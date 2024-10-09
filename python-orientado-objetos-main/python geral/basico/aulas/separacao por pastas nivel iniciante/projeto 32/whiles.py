sexo = str(input("informe seu sexo: ")).strip().upper()[0]  #strip tira espacos em branco e upper coloca em maiusculo e [0] pega so a primeira posicao
sexos = str(input("informe seu sexo: ")).strip().upper()[0]
while sexo not in "MmFf":   #mesma coisa de ["M","m","F","f"]
    sexo = str(input("informe seu sexo corretamente: ")).strip().upper()[0]
while sexos not in ["f","M","F","m"]:
    sexos = str(input("informe seu sexo corretamente: ")).strip().upper()[0]
print(f"sexo {sexo}")
print(f"sexo {sexos}")


resp = str(input('Digite uma letra: ')).strip().upper()[0]
print(resp)
resp = str(input('Digite uma letra: ')).upper().strip()[1]
print(resp)