from pathlib import Path

root_dir = Path("automation\\folders changes\\files")

for path in root_dir.glob("**/*"):
    if path.is_file:
        parent_folder = path.parts
        subfolders = path.parts[1:-1]
        new_file = "-".join(subfolders) + "-" + path.name
        print(new_file)
        new_filepath = path.with_name(new_file)
        path.rename(new_filepath)
