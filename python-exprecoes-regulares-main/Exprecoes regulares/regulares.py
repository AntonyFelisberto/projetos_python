import re #necessario para expressões

string = "teste de expressões regulares"

print(re.search(r'teste',string))
print(re.search(r'teste2',string))

print(re.findall(r'teste',string))
print(re.findall(r'teste2',string))

print(re.sub(r'teste','ABM',string))
print(re.sub(r'teste','ABM',string,count=1)) #count é quantos items substituira

reg = re.compile(r'teste')
print(reg.search(string))
print(reg.findall(string))
print(reg.sub('AAS',string))