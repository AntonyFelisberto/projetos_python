def maior(colecao):
    maior = colecao[0]
    for item in colecao:
        if item > maior:
            maior = item
    return maior

def menor(colecao):
    menor = colecao[0]
    for item in colecao:
        if item < menor:
            menor = item
    return menor

print(maior([1,2,3,4,5,6,7,8,49,54,11,1452,0]))
print(maior((1,2,3,4,5,6,7,8,49,54,11,1452,0)))
print(menor((1,2,3,4,5,6,7,8,49,54,11,1452,0)))