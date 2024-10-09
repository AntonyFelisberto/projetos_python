#SEPARAR STRINGS
#[inicio:fim:de_quanto_em_quanto_pula] 

#separando pegando as posições


variavel = "artorias"

#ESPAÇOS CONTAM COMO CARACTER
print(variavel)
print(len(variavel))
print(variavel[-1]) #CARACTER ESPECIFICO DE TRAS
print(variavel[1])  #CARACTER ESPECIFICO
print(variavel[0:]) #INICIO AO FIM
print(variavel[0:5]) #ELE SEMPRE TIRA O INDICE FINAL OU SEJA DO 0 AO 4
print(variavel[-1:-5]) #ELE SEMPRE TIRA O INDICE FINAL OU SEJA DO 0 AO 4
print(variavel[0:len(variavel):1]) #CONTANDO DE UM EM UM
print(variavel[0:len(variavel):2]) #CONTANDO DE 2 EM 2

#PASSOS COM NUMEROS NEGATIVOS INVERTE A STRING
print(variavel[::-1])
print(variavel[-1:-8:-1])
print(variavel[-1:-8:-2])
print(variavel[0:9:-1]) #COM NUMEROS POSITIVOS O PASSO NEGATIVO NÃO FUNCIONA