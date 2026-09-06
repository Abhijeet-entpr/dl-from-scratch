from pathlib import Path
import sys

# Get the directory of the current script: .../projects/nested
script_dir = Path("dl-from-scratch/projects/nested").resolve().parent
print(script_dir)

# Find the repo root by going two directories up:
repo_root = script_dir.parents[0]  # or script_dir.parent.parent

# Add the repo root to sys.path so Python can find 'utils'
sys.path.insert(0, str(repo_root))

# Now this import will work!
print(sys.path)
from utils.stats import RunningStats