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
      # get everything after github.com/ : github.com/owner/repo
      lines = [line.split("github.com/")[-1] for line in lines]
      # remove duplicates
      lines = list(set(lines))
      # remove empty lines
      lines = [line for line in lines if line]

    # write to file
    with open(target_filename, "w") as f:
      for line in lines:
        f.write(f"{line}\n")
    print(f"Saved top {n} packages for {pm} with github scm to {target_filename}")
