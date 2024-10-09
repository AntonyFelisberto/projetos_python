from pathlib import Path

root_dir = Path("automation\\folders changes\\files")
file_paths = root_dir.iterdir()

print(Path.cwd())

for path in file_paths:
    new_filename = "new_"+path.stem+path.suffix
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)