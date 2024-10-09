print("EXIBE O ARGUMENTO NA TELA, NO CASO O ARGUMENTO É ESSA STRING")
print(12,34,56) # O PRINT ASSIM COMO FUNÇÕES RECEBE ARGUMENTOS
"""
# NO PYTHON EXISTEM SEPARADORES QUE NO CASO DÃO UM ESPAÇO ENTRE UM ARGUMENTO E O OUTRO 
# NO CASO O , É UM SEPARADOR POR ISSO AO INVES DE VIRGULA NO PRINT ELE DA UM ESPAÇO
"""
print(12,34,56) 
print(12,34,sep=' ') # USANDO O sep com "" ou '' voce pode definir qual separador voce quer que apareça ao inves do espaço
"""
# A QUESTÃO DA "" OU '' VOCE PODE USAR EM QUALQUER METODO DO MESMO JEITO DO sep
"""
print(12,34,sep="")
print(12,34,sep="@@")
print(12,34,sep="&")
print(12,34,sep="---")
print(12,34,sep="TESTE")

"""
# ARGUMENTOS NOMEADOS E NÃO NOMEADOS
# print(12,34) -> NÃO NOMEADOS POIS NENHUMA VARIAVEL OU OBJETO RECEBEU ELES
# print(sep="&") -> NOMEADO POIS A VARIAVEL RECEBEU UM VALOR
"""

"""
#CARACTERES DE ESCAPE QUE NÃO APARECEM - CHAMADOS DE CRLF

#\n     quebra de linha
#\r     retornar

#GERALMENTE ESSES COMANDOS JA SÃO PADRÕES NO WINDOS POR SE APROXIMAR DO UNIX
"""
print(12,34,sep="TESTE",end="\n#\n#ola\n") #usando os caracteres de escapem o end vai adicionar o item ao fim da linha podendo tanto ser os de escape quanto outros
print(12,34,sep="TESTE",end="\r\n") #usando os caracteres de escapem o end vai adicionar o item ao fim da linha
print(12,34,sep="TESTE",end="\n") #usando os caracteres de escape
print(12,34,sep="TESTE",end="\r") #usando os caracteres de escape

#PYTHON É CASE SENSITIVE OU SEJA CASO UM MÉTODO OU VARIAVEL FOR DECLARADO DIFERENTE DO ATUAL ELE VAI TE DAR ERRO