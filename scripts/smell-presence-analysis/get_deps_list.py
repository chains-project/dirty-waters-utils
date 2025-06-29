import json
from pathlib import Path

BASE_DIR = Path(__file__).parent / "results"
print(f"Base directory: {BASE_DIR}")
get_deps_files = lambda pm: [
    p for p in BASE_DIR.glob(f"runs/{pm}-runs/*/sscs/*/*.json")
    if p.parent.parent.name == "sscs"
]

# Helper function to load unique strings from deps_list.json
def load_deps(files):
    deps = {}
    for path in files:
        with path.open() as f:
            data = json.load(f)
            for dep in data.keys():
                deps[dep] = deps.get(dep, 0) + 1
    return deps

# Split the files
npm_files = get_deps_files("npm")
maven_files = get_deps_files("maven")
print(len(npm_files), "npm files found.")
print(len(maven_files), "maven files found.")

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
