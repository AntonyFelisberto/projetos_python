#ATENÇÃO CASO VOCE NÃO MUDE A VARIAVEL CONDICIONAL DO LOOP ISSO PODE CRIAR UM LOOP INFINITO

i = 10
while i>0:      #COM NUMEROS EM DECRESCENTE
    print(i)
    i=i-1

while i<10:      #COM NUMEROS EM CRESCENTE
    print(i)
    i=i+1

condicao = True
while condicao:
    ...
    condicao = False


while condicao:
    ...
    break

condicao = True
numero = 0
while condicao and numero <5:
    ...
    numero+=1
    continue

linha = 0
coluna=0
while condicao:

    while coluna < 10:
        print(f'{linha=} {coluna=}')
        coluna+=1
        if coluna >= 10:
            condicao = False

    linha+=1