primeiro_valor = input("Digite um valor:")
segundo_valor = input("Digite outro valor:")
terceiro_valor = input("Digite o terceiro valor:")

#EM PYTHON EXISTE O VALOR NONE QUE SIGNIFICA QUE O VALOR NÃO EXISTE

if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    print(f"O primeiro valor de {primeiro_valor} foi o maior valor digitado")
elif segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    print(f"O segundo valor de {segundo_valor} foi o maior valor digitado")
elif terceiro_valor > primeiro_valor and terceiro_valor > segundo_valor:
    print(f"O terceiro valor de {terceiro_valor} foi o maior valor digitado")
else:
    print("Os valores são todos iguais")

#EXISTEM OS TIPOS falsy EM PYTHON QUE SÃO CONSIDERADOS False
#ALGUNS DELES SÃO 0 0.0 ""
print(True and True)
#AVALIAÇÃO DE CURTO CIRCUITO, SE A EXPRESSÃO NO COMEÇO FOR FALSE O PYTHON NÃO CHECA O RESTO E RETORNA False
print(True and False and True)
print(True and 0 and True)
print(bool(''))
print(bool(' '))

escolha = input('E para entrar S para sair: ')
senha = input('Senha de entrada: ')
senhaAtual = "12345678"

if  (escolha.upper() == "E" or escolha.lower() == 'e') and senha == senhaAtual:
    print("Entrada permitida")
else:
    print("Saindo")

print(True or False)
print(0 or False or 0 or "abc" or True) # NO MOMENTO QUE O PYTHON ACHA O "abc" ELE PARA A VALIDAÇÃO POIS JA ACHOU UM True

variavel_vazia_ou_digitada = input("DIGITE UM VALOR: ") or "VOCE NÃO DIGITOU UM VALOR" #CASO O USUARIO NÃO DIGITE NADA VAI COLOCAR O VALOR DO or
print(variavel_vazia_ou_digitada)

variavel_a = 1 or 0             #O or SÓ MUDA O VALOR CASO O VALOR INICIAL DA VARIAVEL SEJA CONSIDERADO False
variavel_b = 0 or 1             #AQUI MUDA POIS O VALOR É False
print(variavel_a, variavel_a)


negacao_de_valores = input("Digite um valor: ")

if not negacao_de_valores:  #CASO A VARIAVEL SEJA VAZIA
    print("Sem valor")
else:
    print("Tem Valor")

print(not False)
print(not True)
print(not 0)
print(not 1)

