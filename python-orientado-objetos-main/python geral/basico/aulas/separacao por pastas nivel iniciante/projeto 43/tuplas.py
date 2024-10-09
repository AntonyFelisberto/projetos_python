lanches = ('Hamburguer','suco','pizza','pudim')
print(lanches)
print(lanches[1:])
print(lanches[:2])
print(lanches[1:3])
print(lanches[-2])
print(lanches[-2:])

print(len(lanches))

for cont in range(0,len(lanches)):
    print(lanches[cont]," posição ",cont)

for posicao,comida in enumerate(lanches):
    print(comida,posicao)

print(sorted(lanches))

a = (2,4,5,5)
b = (4,2,1,4,5,6)
c = a + b
print(c)
print(c.count(4))
print(c.index(2))
print(c.index(2)+1)
print(c.index(2,2)) #achar o 2 a partir da 2 posição

pessoas = (1,2,3,"artorias",77.44)
print(pessoas)
#tupla é imutavel
#lanches[1] = 1

del(lanches[0])
del pessoas

from random import randint
sorteado = (randint(1,11),randint(1,11),randint(1,11),randint(1,11),randint(1,11),randint(1,11),randint(1,11))
print(max(sorteado))
print(min(sorteado))

entradas = (int(input("digite um numero 1:")),int(input("digite um numero 2:")),int(input("digite um numero 3:")))
if 3 in entradas:
    print("existe")