import os
import re
import json
from collections import defaultdict

# Updated pattern: look for the exact label followed by a number
PATTERNS = [
  r":wrench: Packages with inaccessible commit SHA/tag \(⚠️⚠️⚠️⚠️\):\s*(\d+)",
  r":heavy_exclamation_mark: Packages with no source code URL \(⚠️⚠️⚠️\):\s*(\d+)",
  r":no_entry: Packages with repo URL that is 404 \(⚠️⚠️⚠️\):\s*(\d+)",
  r":black_square_button: Packages without build attestation \(⚠️⚠️⚠️\):\s*(\d+)",
  r":unlock: Packages with invalid code signature \(⚠️⚠️⚠️\):\s*(\d+)",
  r":lock: Packages without code signature \(⚠️⚠️\):\s*(\d+)",
  r":x: Packages that are deprecated \(⚠️⚠️\):\s*(\d+)",
  r":alien: Packages that are aliased \(⚠️⚠️\):\s*(\d+)",
]

# Map pattern indices to smell names for better readability
SMELL_TYPES = [
    "inaccessible_commit_sha",
    "no_source_code_url",
    "repo_url_404",
    "no_build_attestation",
    "invalid_code_signature",
    "no_code_signature",
    "deprecated",
    "aliased"
]

# Total pattern is like " ### Total packages in the supply chain: 413"
TOTAL_PATTERN = r"### Total packages in the supply chain:\s*(\d+)"

def load_json_file(path):
    with open(path, "r") as f:
        return json.load(f)

def extract_table_data(md_content, table_start_marker):
    """Extract table data from markdown content."""
    # Find the table section
    table_section_match = re.search(f"{table_start_marker}(.*?)</details>", md_content, re.DOTALL)
    if not table_section_match:
        return []
    
    table_section = table_section_match.group(1)
    
    # Extract the table rows
    rows = []
    in_table = False
    header_row = None
    
    lines = table_section.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line.startswith('|'):
            continue
        
        # If we find the table header
        if line.startswith('|') and line.endswith('|') and not in_table:
            header_row = [col.strip() for col in line.split('|')[1:-1]]  # Remove first and last empty items
            
            # Check if next line is separator
            if i+1 < len(lines) and re.match(r"^\|[\s\-:]+\|[\s\-:]+\|.*$", lines[i+1].strip()):
                in_table = True
                continue
        
        # If we're in the table, process rows (after the separator line)
        elif in_table and line.startswith('|') and line.endswith('|') and ":--" not in line: 
            columns = [col.strip() for col in line.split('|')[1:-1]]  # Remove first and last empty items
            # print(f"Processing row: {columns}")
            if len(columns) == len(header_row):
                row_data = {}
                for j, col in enumerate(columns):
                    # Clean up the column values (remove backticks)
                    clean_col = col.strip('`')
                    row_data[header_row[j]] = clean_col
                rows.append(row_data)
    
    return rows

def parse_markdown_report(md_path):
    """Parse a markdown report file and extract structured information."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    result = {
        "statistics": {},
        "tables": {}
    }
    
    # Extract basic statistics
    total = re.search(TOTAL_PATTERN, content)
    result["statistics"]["total_packages"] = int(total.group(1)) if total else 0
    
    for i, pattern in enumerate(PATTERNS):
        match = re.search(pattern, content)
        smell_type = SMELL_TYPES[i]
        result["statistics"][smell_type] = int(match.group(1)) if match else 0
    
    # Extract tables
    table_markers = [
        ("<summary>List of packages with available source code repos but with inaccessible commit SHAs/tags", "inaccessible_commit_sha"),
        ("<summary>Source code links that could not be found", "no_source_code_url"),
        ("<summary>List of packages without provenance", "no_build_attestation"),
        ("<summary>List of packages without code signature", "no_code_signature"),
        ("<summary>List of packages with an existing but invalid code signature", "invalid_code_signature"),
        ("<summary>List of deprecated packages", "deprecated"),
        ("<summary>List of aliased packages", "aliased"),
        ("<summary>Other info:", "other_info"),
    ]
    
    # Look for additional patterns in the content to accommodate different report formats
    # Some reports might use different wording for the tables
    additional_markers = []
    details_blocks = re.findall(r"<details>\s*<summary>(.*?)</summary>", content)
    
    for block in details_blocks:
        block = block.strip()
        # Skip already covered markers
        if any(marker in block for marker, _ in table_markers):
            continue
            
        # Try to determine what type of smell this details block represents
        if "inaccessible" in block.lower() and "commit" in block.lower():
            additional_markers.append((block, "inaccessible_commit_sha"))
        elif "source code" in block.lower() and ("404" in block.lower() or "not found" in block.lower()):
            additional_markers.append((block, "no_source_code_url"))
        elif "provenance" in block.lower() or "attestation" in block.lower():
            additional_markers.append((block, "no_build_attestation"))
        elif "without code signature" in block.lower():
            additional_markers.append((block, "no_code_signature"))
        elif "invalid" in block.lower() and "signature" in block.lower():
            additional_markers.append((block, "invalid_code_signature"))
        elif "deprecated" in block.lower():
            additional_markers.append((block, "deprecated"))
        elif "alias" in block.lower():
            additional_markers.append((block, "aliased"))
    
    # Combine standard and additional markers
    all_markers = table_markers + additional_markers
    
    for marker, table_name in all_markers:
        # print(f"Extracting table for md_path: {md_path} with marker: {marker}")
        table_data = extract_table_data(content, marker)
        if table_data:  # Only add if we found some data
            result["tables"][table_name] = table_data
    
    # print(f"Other info: {result['tables'].get('other_info', [])}")
    return result

def build_dependency_smell_data(report_data, project_name):
    """Build a dependency smell data structure from the report data."""
    all_packages = set()
    package_smells = defaultdict(set)
    parent_child_relations = defaultdict(set)
    no_github_url = {}
    
    # Process each table to identify packages with smells
    for smell_type, table in report_data["tables"].items():
        for row in table:
            # Extract package name - different tables use different column names
            package_name = None
            
            # Try common column names for package identification
            package_column_names = ["package_name", "package", "name", "dependency"]
            for col_name in package_column_names:
                if col_name in row:
                    package_name = row[col_name]
                    break
            
            # Maven style packages may be in a column containing a colon
            if not package_name:
                for col_name in row.keys():
                    if ':' in col_name and '@' in col_name:
                        package_name = col_name
                        break
            
            # Still no package? Try looking for column with @ symbol which often indicates package@version format
            if not package_name:
                for col_name, value in row.items():
                    if '@' in value and not package_name:
                        package_name = value
                        break
            
            # Skip if no package name found after all attempts
            if not package_name:
                continue
            
            # Clean the package name (remove backticks, quotes)
            package_name = package_name.strip('`\'\" ')
                
            all_packages.add(package_name)
            if smell_type == "no_source_code_url":
                if "github_exists" in row and row["github_exists"] in ["False", False]:
                    package_smells[package_name].add("repo_url_404")
                else:
                    package_smells[package_name].add("no_source_code_url")
            else:
                package_smells[package_name].add(smell_type)
            
            # Check if parent info exists and extract child-parent relationships
            parent_column_names = ["parent", "parents", "depends_on", "dependency_of"]
            parent_str = None
            
            for col_name in parent_column_names:
                if col_name in row:
                    parent_str = row[col_name]
                    break
            
            if parent_str:
                # Clean up the parent string to extract actual package names
                if parent_str != "[]":
                    # Format might be like: `['package1@version', 'package2@version']`
                    # Remove ticks, brackets, and split by commas
                    parent_str = parent_str.strip('`[]\'\" ')
                    if parent_str:
                        # Handle different potential formats
                        if ',' in parent_str:
                            parents = [p.strip('\'"` ') for p in parent_str.split(',')]
                        else:
                            parents = [parent_str]
                            
                        for parent in parents:
                            if parent and parent != "[]":
                                all_packages.add(parent)
                                parent_child_relations[parent].add(package_name)
            
            # If it's the Other info table, we want to extract the github_url column
            if smell_type == "other_info":
                github_url = row.get("github_url")
                if github_url:
                    package_smells[package_name].add(smell_type)
                    no_github_url[package_name] = github_url
    
    # Build the result data structure
    result = {}
    for package in all_packages:
        if package == "None":
            print(f"Skipping package 'None' in {project_name}")
            continue
        direct_smells = list(package_smells.get(package, []))
        tainted_children = []
        
        # Check for children with smells
        if package == "rollup@4.13.0":
            print(f"Found rollup@4.13.0 in {project_name}")
            print(f"parent_child_relations: {parent_child_relations.get(package, [])}")
        for child in parent_child_relations.get(package, []):
            child_smells = list(package_smells.get(child, []))
            if child_smells:
                tainted_children.append({
                    "package": child,
                    "smells": child_smells
                })
        
        # New structure - store project association
        result[package] = {
            "direct_smells": direct_smells,
            "tainted_children": tainted_children,
            "project": project_name  # Add project name to track where this package instance was found
        }
        if package in no_github_url:
            result[package]["github_url"] = no_github_url[package]
    
    return result

def find_markdown_report(folder):
    """Find a markdown report file in the given folder."""
    files = os.listdir(folder)
    md_file = next((f for f in files if f.endswith(".md")), None)
    if md_file:
        return os.path.join(folder, md_file)
    return None

def analyze_project_folder(folder_path):
    """Analyze a single project folder and return dependency smell data."""
    md_path = find_markdown_report(folder_path)
    if not md_path:
        return None
    
    try:
        report_data = parse_markdown_report(md_path)
        project_name = os.path.basename(folder_path)
        report_creation_time = None
        
        # Try to extract project name and report creation time from the report
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Look for project name in the report
            project_name_match = re.search(r"# Software Supply Chain Report of (.*?)(?: - |$)", content)
            if project_name_match:
                project_name = project_name_match.group(1).strip()
                
            # Look for report creation time
            time_match = re.search(r"Report created on (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", content)
            if time_match:
                report_creation_time = time_match.group(1)
        
        # Build dependency data with project name
        dependency_data = build_dependency_smell_data(report_data, project_name)
        
        metadata = {
            "project_name": project_name,
            "report_creation_time": report_creation_time,
            "folder_path": folder_path,
            "total_packages": report_data["statistics"].get("total_packages", 0),
            "total_smells_detected": sum(report_data["statistics"].values()) - report_data["statistics"].get("total_packages", 0)
        }
        
        return {
            "metadata": metadata,
            "packages": dependency_data
        }
    except Exception as e:
        print(f"Error analyzing {folder_path}: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    outcomes_dir = "results/outcomes"
    os.makedirs(outcomes_dir, exist_ok=True)
    configs = [
        ("maven-runs_success.json", "results/runs/maven-runs"),
        ("npm-runs_success.json", "results/runs/npm-runs"),
        ("maven-lockfile-runs_success.json", "results/runs/maven-lockfile-runs"),
        ("shescape-runs_success.json", "results/runs/shescape-runs")
    ]
    
    for json_file, base_dir in configs:
        print(f"\nAnalyzing {json_file}...")
        success_list_path = os.path.join(outcomes_dir, json_file)
        
        # If the success list doesn't exist, create a placeholder for testing
        if not os.path.exists(success_list_path):
            print(f"Success list file not found: {success_list_path}")
            print(f"Creating a placeholder with folders in {base_dir} for testing...")
            
            # Check if base_dir exists
            if os.path.exists(base_dir):
                # Get the list of folders in base_dir
                folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
                with open(success_list_path, "w") as f:
                    json.dump(folders, f)
                print(f"Created placeholder with {len(folders)} folders")
                success_list = folders
            else:
                print(f"Base directory {base_dir} not found. Skipping...")
                continue
        else:
            success_list = load_json_file(success_list_path)
        
        # Initialize structures for package-centric analysis
        all_packages = {}
        projects_metadata = {}
        
        for project_folder in success_list:
            # print(f"Processing project: {project_folder}")
            folder_path = os.path.join(base_dir, project_folder)
            
            if not os.path.exists(folder_path):
                print(f"Project folder not found: {folder_path}")
                continue
                
            result = analyze_project_folder(folder_path)
            if not result:
                print(f"No valid report found or error occurred for: {folder_path}")
                continue
            
            # Store project metadata
            projects_metadata[project_folder] = result["metadata"]
            
            # Aggregate package data across projects
            for package_name, package_data in result["packages"].items():
                if package_name not in all_packages:
                    if "velocity-tools" in package_name:
                        print(f"Found {package_name} in {result['metadata']['project_name']}")
                    # First time seeing this package
                    all_packages[package_name] = {
                        "direct_smells": package_data["direct_smells"],
                        "tainted_children": package_data["tainted_children"],
                        "projects": [result["metadata"]["project_name"]],
                        "occurrence_count": 1,
                    }
                    if "github_url" in package_data:
                        all_packages[package_name]["non_github_url"] = package_data["github_url"]
                else:
                    # Package already seen in another project
                    if "velocity-tools" in package_name:
                        print(f"Found {package_name} in {result['metadata']['project_name']}")
                    existing_package = all_packages[package_name]
                    existing_package["occurrence_count"] += 1
                    
                    # Add to projects list if not already there
                    if result["metadata"]["project_name"] not in existing_package["projects"]:
                        existing_package["projects"].append(result["metadata"]["project_name"])
                    
                    # Merge smells (avoiding duplicates)
                    for smell in package_data["direct_smells"]:
                        if smell not in existing_package["direct_smells"]:
                            existing_package["direct_smells"].append(smell)
                    
                    # Merge tainted children (more complex as we need to avoid duplicates)
                    existing_child_packages = {child["package"] for child in existing_package["tainted_children"]}
                    
                    for child in package_data["tainted_children"]:
                        if child["package"] not in existing_child_packages:
                            existing_package["tainted_children"].append(child)
                        else:
                            # Child already exists, merge smells
                            for existing_child in existing_package["tainted_children"]:
                                if existing_child["package"] == child["package"]:
                                    for smell in child["smells"]:
                                        if smell not in existing_child["smells"]:
                                            existing_child["smells"].append(smell)
        
        # Create output structure
        total_package_occurrences = sum(package["occurrence_count"] for package in all_packages.values())
        average_packages_per_project = total_package_occurrences / len(projects_metadata) if projects_metadata else 0
        package_centric_output = {
            "metadata": {
                "package_manager": base_dir,
                "total_projects": len(projects_metadata),
                "total_unique_packages": len(all_packages),
                "average_packages_per_project": average_packages_per_project,
            },
            "projects": projects_metadata,
            "packages": all_packages
        }
        
        # Save results
        output_file = f"{outcomes_dir}/{base_dir.split('/')[-1]}_dependency_smells_by_package.json"
        with open(output_file, "w") as f:
            json.dump(package_centric_output, f, indent=2)
        print(f"Created package-centric dependency smell report: {output_file}")
        
        # Print a summary
        print(f"\nSummary for {base_dir}:")
        print(f"  Total projects analyzed: {len(projects_metadata)}")
        print(f"  Total unique packages: {len(all_packages)}")
        
        # Count packages with certain properties
        packages_with_smells = sum(1 for p in all_packages.values() if p["direct_smells"])
        packages_with_tainted_children = sum(1 for p in all_packages.values() if p["tainted_children"])
        widely_used_packages = sum(1 for p in all_packages.values() if p["occurrence_count"] > 1)
        
        print(f"  Packages with direct smells: {packages_with_smells}")
        print(f"  Packages with tainted children: {packages_with_tainted_children}")
        print(f"  Packages used in multiple projects: {widely_used_packages}")

if __name__ == "__main__":
    main()