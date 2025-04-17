from util import extract_repo_url, get_command, run_command, api_constructor, make_github_request, check_source_code_by_version
import os
import requests

LIBRARIES_IO_API_KEY = os.getenv("LIBRARIES_IO_KEY")

def get_package_list(pm):
  def parse_npm_from_gist():
    GIST_URL = "https://gist.githubusercontent.com/anvaka/8e8fa57c7ee1350e3491/raw/b6f3ebeb34c53775eea00b489a0cea2edd9ee49c/01.most-dependent-upon.md"
    response = requests.get(GIST_URL)
    # Output will be like:
    # * Date: Fri, 16 Aug 2019 07:31:10 GMT
    # * Input file: `./data/dependenciesGraph.out.graph`

    # # Top 1000 most depended-upon packages

    # 0. [lodash](https://www.npmjs.org/package/lodash) - 69147
    # 1. [chalk](https://www.npmjs.org/package/chalk) - 39816
    # ...

    lines = response.text.split("\n")
    packages = []
    for line in lines:
      if line.startswith("*") or line.startswith("#"):
        continue
      if line.strip() == "":
        continue

      # Split the line by spaces and remove the first element (the number)
      parts = line.split(" ")
      if not parts[0].endswith("."):
        continue
      # The package name is between the first and second brackets
      package_name = parts[1].split("[")[1].split("]")[0]
      # The number of dependents is the last element
      dependents = int(parts[-1])
      packages.append((package_name, dependents))
    return packages
  
  def parse_mvn_from_central():
    LIBRARIES_IO_URL = "https://libraries.io/api/search"
    SIZE = 200
    PAGE = 1
    PER_PAGE = 100  # max per request
    packages = []
    while len(packages) < SIZE:
      params = {
          "platforms": "Maven",
          "sort": "dependents_count",
          "order": "desc",
          "api_key": LIBRARIES_IO_API_KEY,
          "per_page": PER_PAGE,
          "page": PAGE
      }
      resp = requests.get(LIBRARIES_IO_URL, params=params)
      data = resp.json()
      if not data:
        break
      for pkg in data:
        packages.append((pkg["name"], pkg["dependents_count"]))
      PAGE += 1
    return packages[:min(SIZE, len(packages))]

  match pm:
    case "npm":
      # Get the top 1000 most depended-upon packages from npm
      return parse_npm_from_gist()
    case "maven":
      return parse_mvn_from_central()
    case _:
      raise ValueError(f"Unsupported package manager: {pm}")

def get_first_n_with_github_scm(pm, n=50):
  all_packages = get_package_list(pm)
  n_packages = []
  found_github = 0
  for package, dependents in all_packages:
    print(f"Checking {package} with {dependents} dependents")
    # Get the scm command for the package
    command = get_command(pm, package, "scm")
    # Run the command and get the output
    output = run_command(pm, command, "scm")
    if not output:
      print(f"Error running command {command} for package {package}")
      continue
    # Extract the url from the output
    url, extract_message = extract_repo_url(output)
    repo_api, simplified_path, package_full_name, _, version, error_message = api_constructor(package, url)
    # Check if the url is a github url
    if any(msg in extract_message for msg in ["Could not find repository", "Not a GitHub repository"]):
      continue
    print(f"Found {package} with {dependents} dependents and url {url}")
    print(f"Now checking for version -- will try and get the latest published at the registry")
    command = get_command(pm, package, "version")
    output = run_command(pm, command, "version")
    if not output:
      print(f"Error running command {command} for package {package}")
      continue
    version = output.strip()
    print(f"Found latest version {version} for package {package}")

    data = make_github_request(repo_api)
    if data is None:
      continue

    # At this point, it will be a github url
    print(f"Checking if there's a tag or SHA we can use")
    repo_link = f"https://github.com/{simplified_path}".lower()
    source_code_info = check_source_code_by_version(
      package, version, repo_api, repo_link, simplified_path, pm
    )
    if not source_code_info.get("exists", False):
      print(f"Package {package} with version {version} does not exist in the repository")
      continue
    elif source_code_info.get("is_sha", False):
      print(f"Package {package} with version {version} is a hash")
      version = source_code_info.get("sha", version)
    else:
      version = source_code_info.get("url", version).split("tags/")[-1]
      print(f"Package {package} with version {version} is a tag")

    # Checking if they have a package-lock.json or pom.xml
    print(f"Checking if {'package-lock.json' if pm == 'npm' else 'pom.xml'} exists in the repo")
    if pm == "npm":
      check_file = "package-lock.json"
    else:
      check_file = "pom.xml"
    file_url = f"https://raw.githubusercontent.com/{simplified_path}/{version}/{check_file}"
    print(f"Checking for file URL: {file_url}")
    response = requests.get(file_url)
    if response.status_code != 200:
      print(f"File {check_file} does not exist in the repo")
      continue
    print(f"File {check_file} exists in the repo")

    n_packages.append((package, version, dependents, url))
    found_github += 1

    if found_github >= n:
      break
  
  if found_github < n:
    print(f"Found only {found_github} packages with github scm")
  return n_packages

if __name__ == "__main__":
  n = 50
  for pm in ["npm", "maven"]:
  # for pm in ["maven"]:
    print(f"Getting top {n} packages for {pm} with github scm")
    packages = get_first_n_with_github_scm(pm, n=n)
    for package, version, dependents, url in packages:
      print(f"{package}@{version} ({dependents} dependents) - {url}")
    
    # Also pasting into file titled {pm}-top-25.txt
    with open(f"popular-projects/{pm}-top-{n}.txt", "w") as f:
      for package, version, dependents, url in packages:
        f.write(f"{package}@{version} ({dependents} dependents) - {url}\n")
    print(f"Saved top {n} packages for {pm} with github scm to {pm}-top-{n}.txt")
