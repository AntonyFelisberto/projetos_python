from pathlib import Path

pro = Path("automation\\pathlibs\\files\\asbc.txt")
print(type(pro))

if pro.exists():
    with open(pro,"r") as file:
        print(file.read())
else:
    with open(pro,"w") as file:
        file.write("hello")

print(pro.name)
print(pro.stem)
print(pro.suffix)

pro_one = Path("automation\\pathlibs\\files\\")
print(pro_one.iterdir())

for item in pro_one.iterdir():
    print(item)