from pathlib import Path

files_dir = Path("files")

merged = ""
for filepath in files_dir.iterdir():
    with open(filepath,"r") as file:
        content = file.read()
    merged = merged + content + "\n"

print(merged)

with open("merged.csv","w") as file:
    file.write(merged)