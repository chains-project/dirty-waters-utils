import os
import re
import json
from collections import defaultdict
import copy

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
    print(f"Total packages: {result['statistics']['total_packages']}")
    
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
        ("<summary>List of packages with invalid code signature", "invalid_code_signature"),
        ("<summary>List of deprecated packages", "deprecated"),
        ("<summary>List of aliased packages", "aliased"),
        # ("<summary>Other info:", "other_info"),
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
                # check if "github_url" os "No_repo_info_found"; if it is, we keep as is, if not, we switch to repo_url_404
                if "github_url" in row:
                    github_url = row["github_url"]
                    if github_url == "No_repo_info_found":
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

def load_json_file(path):
    """Load a JSON file and return its contents."""
    with open(path, "r") as f:
        return json.load(f)

def analyze_results_folder(base_dir, folder_name):
    """Analyze a single results folder and return dependency smell data."""
    folder_path = os.path.join(base_dir, folder_name)
    
    if not os.path.exists(folder_path):
        print(f"Results folder not found: {folder_path}")
        return None
    
    result = analyze_project_folder(folder_path)
    if not result:
        print(f"No valid report found or error occurred for: {folder_path}")
        return None
    
    return result

def compare_run_results(run1_data, run2_data):
    """Compare two runs and identify differences in packages and smells."""
    if not run1_data or not run2_data:
        return None
    
    # Get all packages from both runs
    run1_packages = {pkg for pkg in run1_data["packages"].keys() if run1_data["packages"][pkg]["direct_smells"]}
    run2_packages = {pkg for pkg in run2_data["packages"].keys() if run2_data["packages"][pkg]["direct_smells"]}
    print(f"Length of run1 packages: {len(run1_packages)}")
    print(f"Length of run2 packages: {len(run2_packages)}")
    
    # Find packages that were removed/added between runs
    removed_packages = run1_packages - run2_packages
    added_packages = run2_packages - run1_packages
    print(f"No. of removed packages: {len(removed_packages)}")
    print(f"No. of added packages: {len(added_packages)}")
    
    # Find packages present in both runs and analyze smell differences
    common_packages = run1_packages.intersection(run2_packages)
    
    smell_changes = {
        "removed_smells": defaultdict(int),  # Count by smell type
        "added_smells": defaultdict(int),    # Count by smell type
        "improved_packages": [],             # Packages with fewer smells
        "unchanged_packages": []             # Packages with same smells
    }
    
    for package in common_packages:
        run1_smells = set(smell for smell in run1_data["packages"][package]["direct_smells"] if smell != "None" and smell != "other_info")
        run2_smells = set(smell for smell in run2_data["packages"][package]["direct_smells"] if smell != "None" and smell != "other_info")
        
        # Count removed and added smells by type
        for smell in run1_smells - run2_smells:
            smell_changes["removed_smells"][smell] += 1
        for smell in run2_smells - run1_smells:
            smell_changes["added_smells"][smell] += 1
        
        # Categorize package changes
        if len(run1_smells) > len(run2_smells):
            smell_changes["improved_packages"].append({
                "package": package,
                "before_smells": list(run1_smells),
                "after_smells": list(run2_smells),
                "removed_smells": list(run1_smells - run2_smells)
            })
        elif run1_smells == run2_smells:
            smell_changes["unchanged_packages"].append({
                "package": package,
                "smells": list(run1_smells)
            })
    
    # Analyze packages that were completely removed or added
    removed_package_details = []
    for package in removed_packages:
        removed_package_details.append({
            "package": package,
            "smells": run1_data["packages"][package]["direct_smells"]
        })
    
    added_package_details = []
    for package in added_packages:
        added_package_details.append({
            "package": package,
            "smells": run2_data["packages"][package]["direct_smells"]
        })
    
    # Count total smells before and after
    total_smells_before = sum(len(run1_data["packages"][pkg]["direct_smells"]) for pkg in run1_packages)
    total_smells_after = sum(len(run2_data["packages"][pkg]["direct_smells"]) for pkg in run2_packages)
    
    # Count by smell type before and after
    smell_counts_before = defaultdict(int)
    smell_counts_after = defaultdict(int)
    
    for pkg in run1_packages:
        for smell in run1_data["packages"][pkg]["direct_smells"]:
            smell_counts_before[smell] += 1
    
    for pkg in run2_packages:
        for smell in run2_data["packages"][pkg]["direct_smells"]:
            smell_counts_after[smell] += 1
    
    comparison_result = {
        "total_packages_before": run1_data["metadata"]["total_packages"],
        "total_packages_after": run2_data["metadata"]["total_packages"],
        "total_smells_before": total_smells_before,
        "total_smells_after": total_smells_after,
        "smell_counts_before": dict(smell_counts_before),
        "smell_counts_after": dict(smell_counts_after),
        "removed_packages": removed_package_details,
        "added_packages": added_package_details,
        "smell_changes": smell_changes
    }
    
    return comparison_result

def main():
    # Define configs for package managers to analyze
    configs = [
        "maven-lockfile-runs",
        # "shescape-runs"
    ]
    
    outcomes_dir = "results/outcomes"
    os.makedirs(outcomes_dir, exist_ok=True)
    
    for base_dir in configs:
        print(f"\nAnalyzing {base_dir}...")
        success_list_path = os.path.join(outcomes_dir, f"{base_dir}_success.json")
        
        try:
            # Load the success list with three folder names
            if os.path.exists(success_list_path):
                success_list = load_json_file(success_list_path)
            else:
                print(f"Success list file not found: {success_list_path}")
                # Create a placeholder for testing if needed
                continue
            
            if len(success_list) != 3:
                print(f"Expected 3 runs in success list, found {len(success_list)}. Skipping...")
                continue
            
            # Define the three runs (before action, after without config, after with config)
            success_list = sorted(success_list)  # Ensure consistent order
            run_before = success_list[0]
            run_after_no_config = success_list[1]
            run_after_with_config = success_list[2]
            
            # Analyze each run
            print(f"Analyzing run before action: {run_before}")
            run1_data = analyze_results_folder(f"results/runs/{base_dir}", run_before)
            
            print(f"Analyzing run after action (no config): {run_after_no_config}")
            run2_data = analyze_results_folder(f"results/runs/{base_dir}", run_after_no_config)
            
            print(f"Analyzing run after action (with config): {run_after_with_config}")
            run3_data = analyze_results_folder(f"results/runs/{base_dir}", run_after_with_config)
            
            # Compare run 1 (before) vs run 2 (after, no config)
            comparison_1_2 = compare_run_results(run1_data, run2_data)
            if comparison_1_2:
                output_file = os.path.join(outcomes_dir, f"{base_dir}_comparison_before_vs_after_no_config.json")
                with open(output_file, "w") as f:
                    json.dump(comparison_1_2, f, indent=2)
                print(f"Created comparison report (before vs after no config): {output_file}")
                
                # Generate summary
                print_comparison_summary(comparison_1_2, "Before vs After (No Config)")
            
            # Compare run 1 (before) vs run 3 (after, with config)
            comparison_1_3 = compare_run_results(run1_data, run3_data)
            if comparison_1_3:
                output_file = os.path.join(outcomes_dir, f"{base_dir}_comparison_before_vs_after_with_config.json")
                with open(output_file, "w") as f:
                    json.dump(comparison_1_3, f, indent=2)
                print(f"Created comparison report (before vs after with config): {output_file}")
                
                # Generate summary
                print_comparison_summary(comparison_1_3, "Before vs After (With Config)")
            
            # Compare run 2 (after, no config) vs run 3 (after, with config)
            comparison_2_3 = compare_run_results(run2_data, run3_data)
            if comparison_2_3:
                output_file = os.path.join(outcomes_dir, f"{base_dir}_comparison_after_no_config_vs_after_with_config.json")
                with open(output_file, "w") as f:
                    json.dump(comparison_2_3, f, indent=2)
                print(f"Created comparison report (after no config vs after with config): {output_file}")
                
                # Generate summary
                print_comparison_summary(comparison_2_3, "After (No Config) vs After (With Config)")
            
            # Generate comprehensive HTML report for all comparisons
            generate_html_report(base_dir, run1_data, run2_data, run3_data, 
                               comparison_1_2, comparison_1_3, comparison_2_3,
                               run_before, run_after_no_config, run_after_with_config)
            
        except Exception as e:
            print(f"Error analyzing {base_dir}: {e}")
            import traceback
            traceback.print_exc()

def print_comparison_summary(comparison, title):
    """Print a summary of the comparison results."""
    print(f"\n===== {title} =====")
    print(f"Total packages: {comparison['total_packages_before']} → {comparison['total_packages_after']} " + 
          f"({comparison['total_packages_after'] - comparison['total_packages_before']:+d})")
    print(f"Total smells: {comparison['total_smells_before']} → {comparison['total_smells_after']} " + 
          f"({comparison['total_smells_after'] - comparison['total_smells_before']:+d})")
    
    print("\nSmell changes by type:")
    all_smell_types = set(list(comparison['smell_counts_before'].keys()) + list(comparison['smell_counts_after'].keys()))
    for smell in all_smell_types:
        before = comparison['smell_counts_before'].get(smell, 0)
        after = comparison['smell_counts_after'].get(smell, 0)
        diff = after - before
        print(f"  {smell}: {before} → {after} ({diff:+d})")
    
    print("\nPackage changes:")
    print(f"  Improved packages (fewer smells): {len(comparison['smell_changes']['improved_packages'])}")
    print(f"  Unchanged overall packages: {comparison['total_packages_before'] - (len(comparison['removed_packages']) + len(comparison['added_packages'])) == comparison['total_packages_after']}")
    print(f"  Unchanged smelly packages (same smells): {len(comparison['smell_changes']['unchanged_packages'])}")
    print(f"  Completely removed packages with smells: {len([pkg for pkg in comparison['removed_packages'] if pkg['smells']])}")
    print(f"  Completely added packages with smells: {len([pkg for pkg in comparison['added_packages'] if pkg['smells']])}")

def generate_html_report(base_dir, run1_data, run2_data, run3_data, 
                       comparison_1_2, comparison_1_3, comparison_2_3,
                       run1_name, run2_name, run3_name):
    """Generate a comprehensive HTML report for all comparisons."""
    if not all([run1_data, run2_data, run3_data, comparison_1_2, comparison_1_3, comparison_2_3]):
        print("Missing data. Cannot generate HTML report.")
        return
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dependency Smells Analysis - {base_dir}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1, h2, h3 {{ color: #333; }}
            .comparison-container {{ margin-bottom: 30px; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            .progress-container {{ background-color: #f3f3f3; border-radius: 3px; width: 100%; }}
            .progress-bar {{ height: 20px; border-radius: 3px; }}
            .positive {{ background-color: #4CAF50; }}
            .negative {{ background-color: #f44336; }}
            .neutral {{ background-color: #2196F3; }}
            .summary-card {{ 
                border: 1px solid #ddd; 
                border-radius: 4px; 
                padding: 15px; 
                margin-bottom: 15px; 
                box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
            }}
            .flex-container {{ display: flex; flex-wrap: wrap; gap: 20px; }}
            .stat-box {{ flex: 1; min-width: 200px; padding: 15px; background-color: #f9f9f9; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
            .small-stat {{ min-width: 150px; text-align: center; }}
            .small-stat h3 {{ margin-bottom: 5px; }}
            .small-stat p {{ font-size: 24px; font-weight: bold; margin: 0; }}
            .tab {{ overflow: hidden; border: 1px solid #ccc; background-color: #f1f1f1; }}
            .tab button {{ background-color: inherit; float: left; border: none; outline: none; cursor: pointer; padding: 14px 16px; transition: 0.3s; }}
            .tab button:hover {{ background-color: #ddd; }}
            .tab button.active {{ background-color: #ccc; }}
            .tabcontent {{ display: none; padding: 6px 12px; border: 1px solid #ccc; border-top: none; }}
            #defaultOpen {{ background-color: #ccc; }}
        </style>
    </head>
    <body>
        <h1>Dependency Smells Analysis Report</h1>
        <p><strong>Package Manager:</strong> {base_dir}</p>
        <p><strong>Run Names:</strong></p>
        <ul>
            <li><strong>Run 1 (Before):</strong> {run1_name}</li>
            <li><strong>Run 2 (After, No Config):</strong> {run2_name}</li>
            <li><strong>Run 3 (After, With Config):</strong> {run3_name}</li>
        </ul>
        
        <div class="tab">
            <button class="tablinks" onclick="openTab(event, 'Summary')" id="defaultOpen">Summary</button>
            <button class="tablinks" onclick="openTab(event, 'Comparison1_2')">Before vs After (No Config)</button>
            <button class="tablinks" onclick="openTab(event, 'Comparison1_3')">Before vs After (With Config)</button>
            <button class="tablinks" onclick="openTab(event, 'Comparison2_3')">No Config vs With Config</button>
        </div>
        
        <div id="Summary" class="tabcontent">
            <h2>Summary of Changes</h2>
            
            <div class="summary-card">
                <h3>Overall Package and Smell Counts</h3>
                <div class="flex-container">
                    <div class="stat-box">
                        <h3>Total Packages</h3>
                        <table>
                            <tr>
                                <th>Run</th>
                                <th>Count</th>
                                <th>Change</th>
                            </tr>
                            <tr>
                                <td>Run 1 (Before)</td>
                                <td>{comparison_1_2['total_packages_before']}</td>
                                <td>-</td>
                            </tr>
                            <tr>
                                <td>Run 2 (No Config)</td>
                                <td>{comparison_1_2['total_packages_after']}</td>
                                <td>{comparison_1_2['total_packages_after'] - comparison_1_2['total_packages_before']:+d}</td>
                            </tr>
                            <tr>
                                <td>Run 3 (With Config)</td>
                                <td>{comparison_1_3['total_packages_after']}</td>
                                <td>{comparison_1_3['total_packages_after'] - comparison_1_2['total_packages_before']:+d}</td>
                            </tr>
                        </table>
                    </div>
                    
                    <div class="stat-box">
                        <h3>Total Smells</h3>
                        <table>
                            <tr>
                                <th>Run</th>
                                <th>Count</th>
                                <th>Change</th>
                            </tr>
                            <tr>
                                <td>Run 1 (Before)</td>
                                <td>{comparison_1_2['total_smells_before']}</td>
                                <td>-</td>
                            </tr>
                            <tr>
                                <td>Run 2 (No Config)</td>
                                <td>{comparison_1_2['total_smells_after']}</td>
                                <td>{comparison_1_2['total_smells_after'] - comparison_1_2['total_smells_before']:+d}</td>
                            </tr>
                            <tr>
                                <td>Run 3 (With Config)</td>
                                <td>{comparison_1_3['total_smells_after']}</td>
                                <td>{comparison_1_3['total_smells_after'] - comparison_1_2['total_smells_before']:+d}</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
            
            <div class="summary-card">
                <h3>Smells by Type</h3>
                <table>
                    <tr>
                        <th>Smell Type</th>
                        <th>Run 1 (Before)</th>
                        <th>Run 2 (No Config)</th>
                        <th>Run 3 (With Config)</th>
                        <th>Change (Run 1 to Run 3)</th>
                    </tr>
    """
    
    # Add rows for each smell type
    all_smell_types = set()
    for counts in [comparison_1_2['smell_counts_before'], comparison_1_2['smell_counts_after'], 
                  comparison_1_3['smell_counts_after']]:
        all_smell_types.update(counts.keys())
    
    for smell in sorted(all_smell_types):
        before = comparison_1_2['smell_counts_before'].get(smell, 0)
        after_no_config = comparison_1_2['smell_counts_after'].get(smell, 0)
        after_with_config = comparison_1_3['smell_counts_after'].get(smell, 0)
        diff = after_with_config - before
        
        html_content += f"""
                    <tr>
                        <td>{smell}</td>
                        <td>{before}</td>
                        <td>{after_no_config}</td>
                        <td>{after_with_config}</td>
                        <td>{diff:+d}</td>
                    </tr>
        """
    
    html_content += """
                </table>
            </div>
            
            <div class="summary-card">
                <h3>Package Status Changes</h3>
                <div class="flex-container">
    """
    
    # Add small stat boxes for package changes
    # Count smelly packages (packages with smells) in removed and added packages
    removed_smelly_packages = sum(1 for pkg in comparison_1_3['removed_packages'] if pkg['smells'])
    introduced_smelly_packages = sum(1 for pkg in comparison_1_3['added_packages'] if pkg['smells'])

    status_metrics = [
        ("Improved Packages", len(comparison_1_3['smell_changes']['improved_packages'])),
        ("Unchanged Smelly Packages", len(comparison_1_3['smell_changes']['unchanged_packages'])),
        ("Removed Packages", len(comparison_1_3['removed_packages'])),
        ("Removed Smelly Packages", removed_smelly_packages),
        ("Added Packages", len(comparison_1_3['added_packages'])),
        ("Added Smelly Packages", introduced_smelly_packages)
    ]
    
    for label, value in status_metrics:
        html_content += f"""
                    <div class="stat-box small-stat">
                        <h3>{label}</h3>
                        <p>{value}</p>
                    </div>
        """
    
    html_content += """
                </div>
            </div>
        </div>
    """
    
    # Add tab content for each comparison
    comparisons = [
        ("Comparison1_2", "Before vs After (No Config)", comparison_1_2, "Run 1 (Before)", "Run 2 (After, No Config)"),
        ("Comparison1_3", "Before vs After (With Config)", comparison_1_3, "Run 1 (Before)", "Run 3 (After, With Config)"),
        ("Comparison2_3", "No Config vs With Config", comparison_2_3, "Run 2 (After, No Config)", "Run 3 (After, With Config)")
    ]
    
    for tab_id, title, comparison, before_name, after_name in comparisons:
        html_content += f"""
        <div id="{tab_id}" class="tabcontent">
            <h2>{title}</h2>
            
            <div class="summary-card">
                <h3>Overview</h3>
                <div class="flex-container">
                    <div class="stat-box">
                        <h3>Packages</h3>
                        <p>{comparison['total_packages_before']} → {comparison['total_packages_after']} ({comparison['total_packages_after'] - comparison['total_packages_before']:+d})</p>
                    </div>
                    <div class="stat-box">
                        <h3>Total Smells</h3>
                        <p>{comparison['total_smells_before']} → {comparison['total_smells_after']} ({comparison['total_smells_after'] - comparison['total_smells_before']:+d})</p>
                    </div>
                </div>
            </div>
            
            <div class="summary-card">
                <h3>Smell Changes by Type</h3>
                <table>
                    <tr>
                        <th>Smell Type</th>
                        <th>{before_name}</th>
                        <th>{after_name}</th>
                        <th>Change</th>
                    </tr>
        """
        
        # Add rows for each smell type in this comparison
        all_smells_in_comparison = set(list(comparison['smell_counts_before'].keys()) + 
                                     list(comparison['smell_counts_after'].keys()))
        
        for smell in sorted(all_smells_in_comparison):
            before = comparison['smell_counts_before'].get(smell, 0)
            after = comparison['smell_counts_after'].get(smell, 0)
            diff = after - before
            
            html_content += f"""
                    <tr>
                        <td>{smell}</td>
                        <td>{before}</td>
                        <td>{after}</td>
                        <td>{diff:+d}</td>
                    </tr>
            """
        
        html_content += f"""
            </div>
            
            <div class="summary-card">
                <h3>Improved Packages (Fewer Smells): {len(comparison['smell_changes']['improved_packages'])}</h3>
        """
        
        if comparison['smell_changes']['improved_packages']:
            html_content += """
                <table>
                    <tr>
                        <th>Package</th>
                        <th>Before Smells</th>
                        <th>After Smells</th>
                        <th>Removed Smells</th>
                    </tr>
            """
            
            for pkg in comparison['smell_changes']['improved_packages']:
                html_content += f"""
                    <tr>
                        <td>{pkg['package']}</td>
                        <td>{', '.join(pkg['before_smells'])}</td>
                        <td>{', '.join(pkg['after_smells'])}</td>
                        <td>{', '.join(pkg['removed_smells'])}</td>
                    </tr>
                """
            
            html_content += """
                </table>
            """
        else:
            html_content += "<p>No packages were improved in this comparison.</p>"
        
        html_content += f"""
            </div>
            
            <div class="summary-card">
                <h3>Removed Smelly Packages: {removed_smelly_packages}</h3>
        """

        if comparison['removed_packages']:
            html_content += """
                <table>
                    <tr>
                        <th>Package</th>
                        <th>Previous Smells</th>
                    </tr>
            """
            
            for pkg in comparison['removed_packages']:
                if pkg['smells']:  # Only show packages that had smells
                    html_content += f"""
                        <tr>
                            <td>{pkg['package']}</td>
                            <td>{', '.join(pkg['smells'])}</td>
                        </tr>
                    """
            
            html_content += """
                </table>
            """
        else:
            html_content += "<p>No smelly packages were completely removed in this comparison.</p>"

        html_content += f"""
            </div>
            
            <div class="summary-card">
                <h3>Introduced Smelly Packages: {introduced_smelly_packages}</h3>
        """

        if comparison['added_packages']:
            html_content += """
                <table>
                    <tr>
                        <th>Package</th>
                        <th>Introduced Smells</th>
                    </tr>
            """
            
            for pkg in comparison['added_packages']:
                if pkg['smells']:  # Only show packages that have smells
                    html_content += f"""
                        <tr>
                            <td>{pkg['package']}</td>
                            <td>{', '.join(pkg['smells'])}</td>
                        </tr>
                    """
            
            html_content += """
                </table>
            """
        else:
            html_content += "<p>No new smelly packages were introduced in this comparison.</p>"

        html_content += """
            </div>
        """
        
        html_content += """
            </div>
        </div>
        """
    
    # Add JavaScript for tabs and finish HTML
    html_content += """
        <script>
        function openTab(evt, tabName) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
            }
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }
            document.getElementById(tabName).style.display = "block";
            evt.currentTarget.className += " active";
        }
        
        // Get the element with id="defaultOpen" and click on it
        document.getElementById("defaultOpen").click();
        </script>
    </body>
    </html>
    """
    
    # Write HTML report to file
    html_file = os.path.join("results", "outcomes", f"{base_dir}_analysis_report.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Generated HTML report: {html_file}")

if __name__ == "__main__":
    main()
