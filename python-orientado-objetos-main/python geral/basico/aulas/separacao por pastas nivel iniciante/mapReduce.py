from functools import reduce

notas = [1.2,3.4,6.7,1.6,8.9]

for i,nota in enumerate(notas):
    notas[i] = nota + 1.5

for i in range(len(notas)):
    notas[i] = nota + 1.5

print(notas)

def mais_um_meio(nota):
    return nota + 1.5

def somar(delta):
    def notas(nota):
        return nota + delta
    return notas

nova_nota = [1.2,3.4,6.7,1.6,8.9]
nova_notas = map(mais_um_meio,nova_nota)
print(nova_notas)

nova_nota = [1.2,3.4,6.7,1.6,8.9]
nova_notas = map(somar(1.5),nova_nota)
print(nova_notas)

def somar_tudo(a,b):
    return a + b

total = reduce(somar_tudo,nova_nota,0) #reduce vai iterar o array
print(total)