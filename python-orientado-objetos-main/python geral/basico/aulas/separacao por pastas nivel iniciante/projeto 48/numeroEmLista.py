
numeros = list()

while True:
    n = int(input("Digite os valores "))
    if n not in numeros:
        numeros.append(n)
    else:
        print("valor ja encontrado")
    r = str(input("QUER CONTINUAR S OU N"))
    if r == 'Nn':
        break

numeros.sort()

