#FORMAS DE ESCREVER VARIAVEIS
uma = "QUANDO É SÓ UMA PALAVRA É TUDO MINUSCULO"
mais_de_uma_palavra_se_usa_o_underline = 1

CONSTANTES_SAO_EM_MAIUSCULO_PARA_DIZER_PARA_NAO_ATRIBUIR_OUTRO_VALOR = 10

if 1 < CONSTANTES_SAO_EM_MAIUSCULO_PARA_DIZER_PARA_NAO_ATRIBUIR_OUTRO_VALOR:
    print("ok")

if 11 >= (CONSTANTES_SAO_EM_MAIUSCULO_PARA_DIZER_PARA_NAO_ATRIBUIR_OUTRO_VALOR - 10):
    print("right")

#\ é usada para quebrar linhas em condicionais
#usando o \ mesmo dando tabs ou enters ele entende que é continuação do anterior
if 11 <= 55 and \
    CONSTANTES_SAO_EM_MAIUSCULO_PARA_DIZER_PARA_NAO_ATRIBUIR_OUTRO_VALOR > 5 and\
        CONSTANTES_SAO_EM_MAIUSCULO_PARA_DIZER_PARA_NAO_ATRIBUIR_OUTRO_VALOR >= 10:
    print("od")

criando_variavel_condicional_para_resumir_if = 11 > 15 or (120 >= 100 and 400 > 150)

if criando_variavel_condicional_para_resumir_if:
    print("passou pela condicao")