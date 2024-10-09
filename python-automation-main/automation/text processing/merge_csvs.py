from pathlib import Path

files_dir = Path("files")

merged = ""
for index,filepath in enumerate(files_dir.iterdir()):
    with open(filepath,"r") as file:
        content = file.read()
        new_content = content[1:]
        
    if index ==0:
        content = "".join(content)
        merged = merged + content + "\n"
    else:
        new_content = "".join(new_content)
        merged = merged + new_content + "\n"

print(merged)

with open("merged.csv","w") as file:
    file.write(merged)