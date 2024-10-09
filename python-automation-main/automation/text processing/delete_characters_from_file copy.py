
with open("automation\\text processing\\files\\file3.csv", "r") as file:
    content = file.read()

modified_content = content[:-1]

with open("automation\\text processing\\files\\file.csv", "w") as file:
    file.write(modified_content)