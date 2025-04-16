# Code taken and/or adapted from dirty-waters (github.com/chains-project/dirty-waters)

import subprocess
import re
import logging
import os
import requests
import time
from typing import Dict, List, Optional
import xmltodict


TIMEOUT = 60
GITHUB_URL_PATTERN = re.compile(r"(github.*)", re.IGNORECASE)
github_token = os.getenv("GITHUB_API_TOKEN")
headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github.v3+json",
}

def extract_repo_url(repo_info: str) -> str:
    """Extract GitHub repository URL from repository information."""
    url = repo_info
    if "https" not in repo_info:
        # cases such as git@github:apache/maven-scm, we just remove the :
        url = url.replace(":/", "/")
    else:
        # could be a redirect, so we'll make a request to the URL to get the final URL
        match = GITHUB_URL_PATTERN.search(url)
        if not match:
            try:
                url = requests.head(url, allow_redirects=True).url
            except requests.exceptions.RequestException:
                logging.warning(f"Could not check for redirections, was using {url}")
    url = url.replace(":", "/")
    match = GITHUB_URL_PATTERN.search(url)
    if not match:
        return repo_info, "Not a GitHub repository"

    # if there is a match, there's still the possibility of the scm url having been
    # put in a different form, e.g.,
    # github.com/apache/maven-scm/tree/maven-scm-2.1.0/maven-scm-providers/maven-scm-providers-standard
    # from here, we only want the URL up until the second-most directory after github.com
    url = match.group(0)
    parts = url.split("/")
    joined = "/".join(parts[:3]) if len(parts) > 3 else url
    joined = joined if not joined.endswith(".git") else joined[:-4]
    return joined, "GitHub repository"


def get_command(pm: str, package: str, purpose: str = "scm") -> List[str]:
    """Get the appropriate command to find a package's source code locations for the package manager."""
    js_info = "version" if purpose == "version" else "repository.url"
    if pm == "yarn-berry" or pm == "yarn-classic":
        return ["yarn", "info", package.replace("@npm:", "@"), js_info, "--silent"]
    elif pm == "pnpm":
        # for cases like @babel/helper-create-class-features-plugin@7.25.9(@babel/core@7.26.10),
        # we look for the repository of the package inside parentheses
        if "(" in package:
            package = package.split("(")[1].split(")")[0]
        return ["pnpm", "info", package.replace("@npm:", "@"), js_info]
    elif pm == "npm":
        return ["npm", "info", package.replace("@npm:", "@"), js_info]
    elif pm == "maven":
        group_id, artifact_id = package.split(":")
        return [
            "mvn",
            "org.apache.maven.plugins:maven-help-plugin:3.5.1:evaluate",
            f"-Dexpression=project",
            f"-Dartifact={group_id}:{artifact_id}",
            "-q",
            "-DforceStdout",
        ]
    raise ValueError(f"Unsupported package manager: {pm}")


def run_command(pm, command, purpose="scm"):
    def run_npm_command(command):
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                timeout=TIMEOUT,
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            logging.warning(
                f"Command {command} timed out after {TIMEOUT} seconds",
            )
            return None
        except subprocess.CalledProcessError as e:
            logging.warning(f"Command {command} failed: {e}")
            return None

    def run_maven_command(command):
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                timeout=TIMEOUT,
            )
            output = result.stdout
            if output:
                parsed_content = xmltodict.parse(output)
                locations = [
                    parsed_content.get("project", {}).get("scm", {}).get("url", ""),
                    parsed_content.get("project", {}).get("scm", {}).get("connection", ""),
                    parsed_content.get("project", {}).get("scm", {}).get("developerConnection", ""),
                    parsed_content.get("project", {}).get("url", ""),
                ] if purpose == "scm" else [
                    parsed_content.get("project", {}).get("version", ""),
                ]
                return next((loc for loc in locations if loc), None)

        except subprocess.TimeoutExpired:
            logging.warning(
                f"Command {command} timed out after {TIMEOUT} seconds",
            )
            return None
        except subprocess.CalledProcessError as e:
            logging.warning(f"Command {command} failed: {e}")
            return None

    if pm == "npm" or pm == "yarn-berry" or pm == "yarn-classic" or pm == "pnpm":
        return run_npm_command(command)
    elif pm == "maven":
        return run_maven_command(command)
    raise ValueError(f"Unsupported package manager: {pm}")

def construct_tag_format(tag, package_name, repo_name):
    _, repo_name = repo_name.split("/")  # splits owner and repo name
    project_name = repo_name.split("-")[-1]  # deals with lots of maven-<project_name> repos (e.g., surefire, etc)
    tag_formats = set(
        [
            f"{tag}",
            f"v{tag}",
            f"v_{tag}",
            f"r{tag}",
            f"release-{tag}",
            f"parent-{tag}",
            # Below: further tag formats found in the AROMA paper, table 3: https://dl.acm.org/doi/pdf/10.1145/3643764
            f"release/{tag}",
            f"{tag}-release",
            f"v.{tag}",
        ]
        + [
            f"{name}{suffix}"
            for name in [package_name, repo_name, project_name]
            for suffix in [f"@{tag}", f"-v{tag}", f"_v{tag}", f"-{tag}", f"_{tag}"]
        ]
    )

    only_package_name, artifact_id_parts = None, None
    if "/" in package_name:  # NPM-based
        only_package_name = package_name.split("/")[1]
    elif ":" in package_name:  # Maven based
        only_package_name = package_name.split(":")[1].split("@")[0]
        # p1, p2, p3 from AROMA
        artifact_id_parts = only_package_name.split("-")

    if only_package_name:
        tag_formats.add(f"{only_package_name}@{tag}")
        tag_formats.add(f"{only_package_name}-v{tag}")
        tag_formats.add(f"{only_package_name}-{tag}")
        tag_formats.add(f"{only_package_name}_{tag}")
    if artifact_id_parts and len(artifact_id_parts) > 1:
        # p1, p2, p3 from AROMA
        # needs to be reversed with [::-1] because p1 is actually the last element, p2 the 2nd to last, etc
        tag_formats.update(["-".join(artifact_id_parts[::-1][: i + 1]) + tag for i in range(len(artifact_id_parts))])

    return tag_formats


def find_existing_tags_batch(tag_formats, repo_name):
    # Get all tags in one request; MAY FAIL if the repo has too many tags
    tags_url = f"https://api.github.com/repos/{repo_name}/git/refs/tags"
    response = make_github_request(tags_url)

    if not response:
        return []
    elif response == 504:
        for tag_format in tag_formats:
            response = make_github_request(f"{tags_url}/{tag_format}")
            if response:
                return [tag_format]
        return []

    # Create a map of all tags
    all_tags = {ref["ref"].replace("refs/tags/", ""): ref for ref in response}

    # Find the matching tag formats
    matching_tags = []
    for tag_format in tag_formats:
        if tag_format in all_tags:
            matching_tags.append(tag_format)

    return matching_tags if matching_tags else []


def check_source_code_by_version(package_name, version, repo_api, repo_link, simplified_path, package_manager):
    def check_git_head_presence(package_name, version):
        # In NPM-based packages, the registry may contain a gitHead field in the package's metadata
        # Although it's not mandatory to have it, if it's present, it's the best way to check
        # the package's source code for the specific version
        try:
            response = requests.get(f"https://registry.npmjs.org/{package_name}/{version}", timeout=20)
            response.raise_for_status()
            data = response.json()
            git_head = data.get("gitHead", "")
            return git_head
        except requests.RequestException as e:
            logging.error(f"Error checking gitHead presence: {str(e)}")
            return False

    source_code_info = {
        "exists": False,
        "tag_version": version,
        "is_sha": False,
        "sha": None,
        "url": None,
        "message": "No tags found in the repo",
        "status_code": 404,
    }
    if package_manager in ["yarn-berry", "yarn-classic", "pnpm", "npm"]:
        if git_head := check_git_head_presence(package_name, version):
            try:
                response = make_github_request(f"{repo_api}/commits/{git_head}", max_retries=2)
                if response:
                    logging.info(f"gitHead {git_head} found in {repo_link}")
                    return {
                        "exists": True,
                        "tag_version": version,
                        "is_sha": True,
                        "sha": git_head,
                        "url": None,
                        "message": "gitHead found in package metadata",
                        "status_code": 200,
                    }
                else:
                    logging.warning(f"gitHead {git_head} not found in {repo_link}, checking tags")
                    source_code_info = {
                        "exists": False,
                        "tag_version": version,
                        "is_sha": True,
                        "sha": git_head,
                        "url": None,
                        "message": f"gitHead {git_head} not found in {repo_link}",
                        "status_code": 404,
                    }
            except Exception as e:
                logging.error(f"Error checking gitHead in repo: {str(e)}")
        else:
            logging.warning(f"gitHead not found in {package_name} {version} metadata")
    else:
        logging.warning(
            f"Package manager {package_manager} not supported for gitHead checking, will proceed with tags"
        )

    have_no_tags_check_api = f"{repo_api}/tags"
    have_no_tags_response = requests.get(have_no_tags_check_api, headers=headers)
    have_no_tags_response_status_code = have_no_tags_response.status_code
    have_no_tags_data = have_no_tags_response.json()

    release_tag_exists = False
    if len(have_no_tags_data) == 0:
        logging.warning(f"No tags found for {package_name} in {repo_api}")
        release_tag_url = None
        message = "No tags found in the repo"
        status_code_release_tag = have_no_tags_response_status_code
    else:
        tag_possible_formats = construct_tag_format(version, package_name, repo_name=simplified_path)
        existing_tag_format = find_existing_tags_batch(tag_possible_formats, simplified_path)
        logging.info(f"Existing tag format: {existing_tag_format}")
        if existing_tag_format:
            existing_tag_format = existing_tag_format[0]
            release_tag_exists = True
            release_tag_url = f"{repo_api}/git/ref/tags/{existing_tag_format}"
            message = f"Tag {existing_tag_format} is found in the repo"
            status_code_release_tag = 200
        else:
            logging.warning(f"Tag {version} not found in {repo_api}")
            release_tag_url = None
            message = f"Tag {version} not found in the repo"
            status_code_release_tag = 404

    source_code_info.update(
        {
            "exists": release_tag_exists,
            "tag_version": version,
            "url": release_tag_url,
            "message": message,
            "status_code": status_code_release_tag,
        }
    )

    return source_code_info


def api_constructor(package_name, repository):
    repo_url = repository.replace("https://", "").replace("http://", "").replace("/issues", "")

    # simplified_path = repo_url.replace("github.com/", "").split('#')[0].split('tree/master')[0].rstrip('/')
    repo_url = repo_url.split("#")[0]
    match = re.search(r"github\.com[:/](.*?)/(.*?)(?:/|$)", repo_url)
    if match:
        simplified_path = f"{match.group(1)}/{match.group(2)}"
    else:
        simplified_path = ""

    if simplified_path.endswith(".git"):
        simplified_path = simplified_path[:-4]

    repo_api = f"https://api.github.com/repos/{simplified_path}"

    error_message = None

    try:
        package_name = package_name.replace("npm:", "")
        parts = package_name.split("@")
        package_full_name = None
        name = None
        version = None

        if len(parts) > 2 or package_name.startswith("@"):
            package_full_name = f"@{parts[1]}"
            _, name = parts[1].split("/")  # scope,name
            version = parts[2]

        elif len(parts) == 2:
            if "/" in parts[1]:
                package_full_name = parts[0]
                scope, name = parts[0].split("/")
                version = parts[1]
            else:
                package_full_name = parts[0]
                name = parts[0]
                version = parts[1]

    except (ValueError, TypeError, AttributeError) as e:
        error_message = f"[INFO][api_constructor] Error: {str(e)}"
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"

    return repo_api, simplified_path, package_full_name, name, version, error_message

def make_github_request(
    url: str,
    method: str = "GET",
    headers: Dict = headers,
    json_data: Optional[Dict] = None,
    max_retries: int = 1,
    retry_delay: int = 2,
    timeout: int = 20,
    sleep_between_requests: int = 0,
    silent: bool = False,
) -> Optional[Dict]:
    """
    Make a HTTP request with retry logic and rate limiting handling.

    Args:
        url (str): HTTP URL
        method (str): HTTP method ("GET" or "POST")
        headers (Dict): Request headers
        json_data (Optional[Dict]): JSON payload for POST requests
        max_retries (int): Maximum number of retry attempts
        retry_delay (int): Base time to wait between retries in seconds
        timeout (int): Request timeout in seconds
        silent (bool): Whether to suppress error logging

    Returns:
        Optional[Dict]: JSON response or None if request failed
    """
    for attempt in range(max_retries):
        try:
            response = requests.request(method=method, url=url, headers=headers, json=json_data, timeout=timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            time.sleep(sleep_between_requests)
            if isinstance(e, requests.exceptions.HTTPError) and (
                e.response.status_code in [429, 403] or "rate limit" in e.response.text.lower()
            ):
                if attempt == max_retries - 1:
                    if not silent:
                        logging.error(f"Failed after {max_retries} attempts due to rate limiting: {e}")
                    return None

                # Get rate limit reset time and wait
                reset_time = int(e.response.headers.get("X-RateLimit-Reset", 0))
                wait_time = max(reset_time - int(time.time()), 0) + 1
                if not silent:
                    logging.warning(f"Rate limit exceeded. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                # Handle other errors
                if not silent:
                    logging.warning(f"Request failed: {e}")
                if attempt == max_retries - 1:
                    if e.response.status_code in [
                        502,
                        504,
                    ]:  # timeout, sometimes happens when the request is too large (e.g., too many tags)
                        return 504
                    return None
                time.sleep(retry_delay * (attempt + 1))

    return None

# Below, code is written specifically for this project
