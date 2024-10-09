#FLAGS SÃO FORMAS DE VERIFICAR SE ALGUM TRECHO FOI EXECUTADO
condicao = False
maneira_correta_de_colocar_uma_flag = None #DEFINIU NENHUM VALOR A VARIAVEL

if condicao:
    passou_no_if = "NUNCA COLOQUE UMA VARIAVEL FLAG EM CONDICIONAIS POIS QUANDO FOR EM OUTRA CONDICAO ELA DARA ERRO"
    maneira_correta_de_colocar_uma_flag = "CORRETO"
    print("True")
else:
    passou_no_if = None #PARA NÃO DAR ERRO NO TRY,POIS CASO CAISE NO TRY E A VAR NÃO EXISTISE DARIA ERRO
    print("false")

try:
    print(passou_no_if)
finally:
    print(maneira_correta_de_colocar_uma_flag,maneira_correta_de_colocar_uma_flag is None)          #is é usado quando uma variavel foi dado como none então o is verifica se continua assim, mas pode ser usado para ver se é de outro tipo tambem 
    print(maneira_correta_de_colocar_uma_flag,maneira_correta_de_colocar_uma_flag is not None)      #is not verifica se um valor não é daquele tipo