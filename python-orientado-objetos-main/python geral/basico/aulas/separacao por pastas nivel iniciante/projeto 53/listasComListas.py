num = [[],[]]
valor = 0
for cont in range(1,8):
    valor = int(input(f"digite o {cont} valor: "))
    if valor % 2 == 0:
        #num.append(valor) #se fosse adicionado assim ele adicionaria fora do array de listas
        num[0].append(valor)
    else:
        num[1].append(valor)

#num.sort() #vai ordenar toda a lista
num[0].sort() #vai ordenar a posição especifica do array
num[1].sort()
print(f"OS VALORES PARES FORAM {num[0]}")
print(f"OS VALORES IMPARES FORAM {num[1]}")