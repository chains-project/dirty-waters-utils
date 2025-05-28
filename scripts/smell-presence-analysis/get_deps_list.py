import json
from pathlib import Path

BASE_DIR = Path(__file__).parent / "results"
print(f"Base directory: {BASE_DIR}")
DEPS_FILES = list(BASE_DIR.glob("runs/*/*/sscs/*/deps_list.json"))

# Sort paths to ensure consistent file ordering
DEPS_FILES.sort()

# Sanity check
if len(DEPS_FILES) < 81:
    raise ValueError(f"Expected at least 81 deps_list.json files, found {len(DEPS_FILES)}.")
print(f"Found {len(DEPS_FILES)} deps_list.json files.")

# Helper function to load unique strings from deps_list.json
def load_deps(files):
    deps = {}
    for path in files:
        with path.open() as f:
            data = json.load(f)
            if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
                raise ValueError(f"Invalid JSON format in: {path}")
            for dep in data:
                deps[dep] = deps.get(dep, 0) + 1
    return deps

# Split the files
npm_files = DEPS_FILES[:42]
maven_files = DEPS_FILES[42:]

# Load sets
npm_deps = load_deps(npm_files)
maven_deps = load_deps(maven_files)

# Save outputs
with open("npm-deps-list.json", "w") as f:
    json.dump({k: npm_deps[k] for k in sorted(npm_deps)}, f, indent=2)

with open("maven-deps-list.json", "w") as f:
    json.dump({k: maven_deps[k] for k in sorted(maven_deps)}, f, indent=2)

print(f"Saved npm-deps-list.json with {len(npm_deps)} entries.")
print(f"Saved maven-deps-list.json with {len(maven_deps)} entries.")
