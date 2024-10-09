#RECEBENDO DADOS DE USUARIO ATRAVES DO input
nome = input("Qual seu nome ? ")
print(f'O seu nome é {nome}')
print(f'O seu nome é {nome=}') #QUANDO SE USA variavel= ELE MOSTRA A VARIAVEL E O VALOR DELA

numero_um = int(input("Digite um numero :")) #CASO O USUARIO DIGITAR UMA LETRA O PROGRAMA QUEBRA
numero_dois = int(input("Digite outro numero :"))
print(f"A {nome} soma dos numeros é :{numero_um + numero_dois}")

numero_um_nao_convertido = input("Digite um numero :") 
numero_dois_nao_convertido = input("Digite outro numero :")
variavel_para_converter_numero_um = int(numero_um_nao_convertido) #CASO O USUARIO DIGITAR UMA LETRA O PROGRAMA QUEBRA AQUI
variavel_para_converter_numero_dois = int(numero_dois_nao_convertido)