import os
import time
import subprocess
import json

def check_run_directories(base_dir):
    success_count = 0
    error_count = 0
    success_folders = []
    failed_folders = []

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(folder_path):
            has_markdown = any(f.endswith('.md') for f in os.listdir(folder_path))
            if has_markdown:
                success_count += 1
                success_folders.append(folder_name)
            else:
                error_count += 1
                failed_folders.append(folder_name)

    return success_count, error_count, success_folders, failed_folders

def main():
    for run_scope in ['maven-runs', 'npm-runs', 'maven-lockfile-runs', 'shescape-runs']:
        print(f"\nChecking {run_scope}...")
        success, error, successes, failures = check_run_directories(f"results/runs/{run_scope}")
        print(f"Successes: {success}")
        if successes:
            print("Successful folders:")
            for folder in successes:
                print(f"  - {folder}")
            # Put the successful folders in a JSON file
            with open(f"results/outcomes/{run_scope}_success.json", 'w') as f:
                json.dump(successes, f, indent=4)
        print(f"Errors: {error}")
        if failures:
            print("Failed folders:")
            for folder in failures:
                print(f"  - {folder}")
            # Put the failed folders in a JSON file
            with open(f"results/outcomes/{run_scope}_failures.json", 'w') as f:
                json.dump(failures, f, indent=4)
        else:
            print("No failed folders.")

if __name__ == "__main__":
    main()
