from pathlib import Path

root_dir = Path("files")
files_paths = root_dir.iterdir()

for path in files_paths:
    for filepath in path.iterdir():
        print(filepath)

root_dir = Path("files")
files_paths = root_dir.glob("**/*")

for path in files_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + "-" + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)