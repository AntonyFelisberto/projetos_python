import random
n_um = str(input("primeiro aluno "))
n_dois = str(input("segundo aluno "))
n_tres = str(input("terceiro aluno "))
n_quatro = str(input("quarto aluno "))
lista = [n_um,n_dois,n_tres,n_quatro]
random.shuffle(lista)
print(f"o embaralhamento ficou : {lista}")