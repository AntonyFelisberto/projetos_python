nome = "asd,aaa,www"
lista = [1,2,3,4,5,"aaa","bbbb",True]

print(nome[1])
print(nome[::-1]) #invertendo tudo
print(lista)
print(lista[0])
print(lista[0])
print(lista[0:2])
print(lista[-1])
print(lista[-1:-4:-1]) #DO MENOS UM AO -4 DE 1 EM UM
print(lista[0:4:-1])

lista[1] = 0
lista.append(11)
lista.remove("aaa")
lista.pop()
lista.insert(0,"my")
frase_separada_por_virgula = nome.split(",")
numero_de_vezes_que_valor_aparece_na_lista = lista.count(1)
lista.clear()