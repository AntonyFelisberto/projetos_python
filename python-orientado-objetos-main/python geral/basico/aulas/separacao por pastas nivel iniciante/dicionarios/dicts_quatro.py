from funcao import *
#from dicts.funcao import * #usando o nome_do_pacote.nome_arquivo
usuarios = {}
opcao = perguntar().upper()
while opcao == "I" or opcao == "P" or opcao =="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar().upper()