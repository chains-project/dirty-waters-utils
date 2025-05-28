if __name__ == "__main__":
  package_managers = ["npm", "maven"]
  n = 50
  for pm in package_managers:
    retrieving_filename = f"popular-projects/{pm}-top-{n}.txt"
    target_filename = f"popular-projects/{pm}-top-{n}-github.txt"
    with open(retrieving_filename, "r") as f:
      lines = f.readlines()
      # remove new line characters
      lines = [line.strip() for line in lines]
      # extract version and github.com/owner/repo
      processed_lines = []
      for line in lines:
        if "github.com/" in line:
          parts = line.split(" - ")
          repo_part = parts[-1].split("github.com/")[-1]
          version_part = line.split("@", 2)[-1].split(" ")[0] if "@" in line else "unknown"
          processed_lines.append(f"{repo_part}@{version_part}")
      # remove duplicates
      processed_lines = list(set(processed_lines))
      # remove empty lines
      processed_lines = [line for line in processed_lines if line]

    # write to file
    with open(target_filename, "w") as f:
      for line in processed_lines:
        f.write(f"{line}\n")
    print(f"Saved top {n} packages for {pm} with github scm to {target_filename}")
