#OUTRO METODO DE FORMATAÇÃO USANDO format
#EM PYTHON TODAS AS VARIAVEIS SÃO OBJETOS, O QUE SIGNIFICA QUE POR TRAS DE CADA OBJETO POSSUI UM MÉTODO ESPECIFICADO PARA ELE
#POR EXEMPLO SE UMA VARIAVEL FOR str E VOCE COLOCAR variavel. VÃO APARECER UMA LISTA DE OPÇÕES DE MÉTODOS DAQUELE OBJETO
a='A'
b='B'
c=1.1

formato = ''.format(a,b,c)  #O DADO DE formtato AINDA É UMA str 
print(formato) #NÃO VAI APARECER POIS NÃO USOU O {} PARA COLOCAR OS DADOS DAS VARIAVEIS

formato_usando_as_variaveis = 'dados = {}{} {}'.format(a,b,c) # PARA USAR OS VALORE DENTRO DO FORMAT VOCE TEM QUE COLOCAR {} PARA CADA VARIAVEL QUE DESEJA INSERIR NA str
print(formato_usando_as_variaveis)

variavel_de_concatenacao = "a={} b={} c={}"
formato_usando_as_variaveis_junto_de_outra_variavel = variavel_de_concatenacao.format(a,b,c)
print(formato_usando_as_variaveis_junto_de_outra_variavel)

variavel_de_concatenacao_com_c_formatado = "c={:.2f}" #FORMATANDO AS VARIAVEIS EM float PARA DUAS CASAS
formatando_variaveis_float = variavel_de_concatenacao_com_c_formatado.format(c) #VAI SUBSTITUIR O :.2f PELO VALOR DA VARIAVEL E VAI COLOCAR O VALOR COM DUAS CASAS DECIMAIS
print(formatando_variaveis_float)

variavel_de_concatenacao = "a={} b={} c={} {}"
#erro = variavel_de_concatenacao.format(a,b,c) # VAI DAR ERRO POIS FORAM ESPECIFICADOS 4 {} PARA 4 VALORES POREM SÓ FORAM PASSADOS 3 DADOS, É A MESMA COISA DE ULTRAPASSAR O NUMERO DE POSIÇÕES DE UM ARRAY

#TUDO NA PROGRAMAÇÃO COMEÇA COM 0 LOGO PARA ESPECIFICAR OS VALORES COMEÇA DE 0 PARA FRENTE
especificando_a_ordem_de_concatenacao = "a={0} a={0} a={1} b={1} c={2}"
variavel_para_guardar_dados_em_ordem_especificada = especificando_a_ordem_de_concatenacao.format(a,b,c) #POR MAIS QUE O NUMERO DE {} SEJA MAIOR QUE O NUMERO DE VARIAVEIS ELE ENTENDE QUAL AS POSIÇÕES DAS VARIAVEIS E SUBSTITUI OS SEUS VALORES
print(variavel_para_guardar_dados_em_ordem_especificada)

especificando_a_ordem_de_concatenacao_junto_com_formatacao = "a={0} b={1} c={2:.2f}"

#PARAMETROS NOMEADOS
#QUANDO VOCE POSSUI UM PARAMETRO NOMEADO VOCE NÃO CONSEGUE UTILIZAR DAS POSIÇÕES DE CADA INDICE

string_para_formatacao_de_dados_nomeados = "a={0} b={1} c={variavel_nomeada_tres:.2f} b={1}" #QUANDO VOCE UTILIZAR A VARIAVEL NOMEADA PRECISA DECLARAR O NOME DELA AO INVES DA POSIÇÃO DA VARIAVEL
formato = string_para_formatacao_de_dados_nomeados.format(
    a,
    b,
    variavel_nomeada_tres=c
)
print(formato)

string_para_formatacao_de_dados_nomeados = "a={0} b={variavel_nomeada_dois} c={variavel_nomeada_tres:.2f} b={variavel_nomeada_dois}" #QUANDO VOCE UTILIZAR A VARIAVEL NOMEADA PRECISA DECLARAR O NOME DELA AO INVES DA POSIÇÃO DA VARIAVEL
formato = string_para_formatacao_de_dados_nomeados.format(
    a,
    variavel_nomeada_dois=b,
    variavel_nomeada_tres=c
)
print(formato)

#A PARTIR DO MOMENTO QUE VOCE USA UMA VARIAVEL NOMEADA AS OUTRAS A FRENTE DELA PRECISAM SER NOMEADAS TAMBEM POIS SENÃO DA ERRO

""" COM ERRO JA QUE SÓ NOMEOU UMA VARIAVEL E NÃO MUDOS OS CAMPOS DA STRING DE FORMATAÇÃO
string_para_formatacao_de_dados_nomeados = "a={0} b={variavel_nomeada_dois} c={variavel_nomeada_tres:.2f} b={variavel_nomeada_dois}" #QUANDO VOCE UTILIZAR A VARIAVEL NOMEADA PRECISA DECLARAR O NOME DELA AO INVES DA POSIÇÃO DA VARIAVEL
formato = string_para_formatacao_de_dados_nomeados.format(
    variavel_nomeada_um=a,
    b,
    c
)
print(formato)
"""

string_para_formatacao_de_dados_nomeados = "a={variavel_nomeada_um} b={variavel_nomeada_dois} c={variavel_nomeada_tres:.2f} b={variavel_nomeada_dois}" #QUANDO VOCE UTILIZAR A VARIAVEL NOMEADA PRECISA DECLARAR O NOME DELA AO INVES DA POSIÇÃO DA VARIAVEL
formato = string_para_formatacao_de_dados_nomeados.format(
    variavel_nomeada_um=a,
    variavel_nomeada_dois=b,
    variavel_nomeada_tres=c
)
print(formato)