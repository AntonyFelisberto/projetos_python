primeiro_valor = input("Digite um valor:")  #QUANDO É DIGITADO UMA LETRA O CODIGO COMPARA OS DOIS PRA VER QUAL É O MAIOR ATRAVES DA TABELA ASC
segundo_valor = input("Digite outro valor:")

if primeiro_valor > segundo_valor:
    print(
            f"Primeiro valor {primeiro_valor} maior que Segundo" # É POSSIVEL USAR DUAS OU MAIS f STRINGS DE FORMATAÇÃO
            f" valor {segundo_valor} "
        )
elif segundo_valor > primeiro_valor:
    print(
            f"Segundo valor {segundo_valor} maior que Primeiro"
            f" valor {primeiro_valor}"
        )
else :
    print("Valores são iguais")

