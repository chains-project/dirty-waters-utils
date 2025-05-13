import os
import re
import json

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
# total pattern is like " ### Total packages in the supply chain: 413"
TOTAL_PATTERN = r"### Total packages in the supply chain:\s*(\d+)"

def load_json_file(path):
    with open(path, "r") as f:
        return json.load(f)

def check_markdown_warning_count(folder):
    counts = {}
    try:
        files = os.listdir(folder)
        md_file = next((f for f in files if f.endswith(".md")), None)
        if not md_file:
            return "No markdown file"

        md_path = os.path.join(folder, md_file)
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        total = re.search(TOTAL_PATTERN, content)
        counts["total"] = int(total.group(1)) if total else 0
        for pattern in PATTERNS:
            match = re.search(pattern, content)
            if match:
                count = int(match.group(1))
                counts[pattern] = count
            else:
                counts[pattern] = 0
        return counts

    except Exception as e:
        return f"Error: {e}"

def analyze_successes(success_list, root_dir):
    found = []
    not_found = []
    counts = {}

    for folder in success_list:
        folder_path = os.path.join(root_dir, folder)
        counts[folder_path] = check_markdown_warning_count(folder_path)

        if counts[folder_path][PATTERNS[0]] > 0:
            found.append(folder)
        else:
            not_found.append(folder)

    print(f"\nTotal with occurrences: {len(found)}")
    print(f"Total without occurrences: {len(not_found)}")

    if found:
        print("Folders with occurrences:")
        for folder in found:
            print(f"  - {folder}")
    # Create a JSON file with the found folders
    with open(os.path.join("outcomes", f"{root_dir}_found.json"), "w") as f:
        json.dump(found, f, indent=4)

    if not_found:
        print("Folders without occurrences:")
        for folder in not_found:
            print(f"  - {folder}")
    # Create a JSON file with the not found folders
    with open(os.path.join("outcomes", f"{root_dir}_not_found.json"), "w") as f:
        json.dump(not_found, f, indent=4)

    # Create a JSON file with the counts
    with open(os.path.join("outcomes", f"{root_dir}_counts.json"), "w") as f:
        json.dump(counts, f, indent=4)

def main():
    outcomes_dir = "outcomes"
    configs = [
        ("npm-runs_success.json", "npm-runs"),
        ("maven-runs_success.json", "maven-runs"),
    ]

    for json_file, base_dir in configs:
        print(f"\nAnalyzing {json_file}...")
        success_list = load_json_file(os.path.join(outcomes_dir, json_file))
        analyze_successes(success_list, base_dir)

if __name__ == "__main__":
    main()
