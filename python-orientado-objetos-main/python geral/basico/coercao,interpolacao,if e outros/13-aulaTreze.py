#FORMATANDO STRINGS

nome = "Antony"
altura = 1.71
peso = 70
imc = peso / (altura * altura)

#PARA FORMATAR STRINGS VOCE COLOCA O f ANTES DE CADA FORMATAÇÃO E A VARIAVEL DENTRO DE {}
#A FORMATAÇÃO PODE SER TANTO EM VARIAVEIS QUANTO EM PRINTS E FUNÇÕES
#NÃO SERVE APENAS PARA STRINGS MAS TAMBEM PARA NUMEROS
variavel_formatada = f"{nome} tem tal nome"
print(variavel_formatada)
print(f"{nome} tem tal nome")
print(f"{nome} tem tal {nome}")
print(f"{nome} tem {altura:.2f}")       #FORMATO COM DUAS CASAS DECIMAIS
print(f"{nome} tem {altura:,.2f}")      #FORMATO COM DUAS CASAS DECIMAIS E COLOCANDO ,