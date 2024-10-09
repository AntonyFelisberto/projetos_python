from pathlib import Path

root_dir = Path("automation\\folders changes\\files")

for path in root_dir.rglob("*.txt"):
    if path.is_file:
        new_filepath = path.with_suffix(".csv")
        path.rename(new_filepath)