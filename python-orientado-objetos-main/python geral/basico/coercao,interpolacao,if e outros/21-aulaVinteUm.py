#operadores in e not in
#STRINGS SÃO ITERAVEIS OU SEJA POSSUEM POSIÇÕES QUE PODEM SER VASCULHADAS
# A-N-T-O-N-Y
# 0 1 2 3 4 5
# -6-5-4-3-2-1  DE TRAS PRA FRENTE O ITERATOR COMEÇA DO -1

nome = "ANTONY"
print(nome[2])
print(nome[-4])
print('Y' in nome) #O in VAI VERIFICAR SE O VALOR ESPECIFICADO ESTA DENTRO DA VARIAVEL
print('Z' in nome)
print(10 * '-')
print('Y' not in nome) #O not in VAI VERIFICAR SE O VALOR ESPECIFICADO NÃO ESTA DENTRO DA VARIAVEL
print('Z' not in nome)
print(' ' in nome)      #VENDO SE A VARIAVEL TEM ESPAÇOS
print(' ' not in nome)

usuario = input("Digite seu nome: ")
find = input("Digite o que deseja encontrar no nome: ")

if find in usuario:
    print(f"{find} se encontra em {usuario}")
else:
    print(f"{find} não se encontra em {usuario}")

if find not in usuario:
    print(f"{find} não se encontra em {usuario}")
else:
    print(f"{find} se encontra em {usuario}")