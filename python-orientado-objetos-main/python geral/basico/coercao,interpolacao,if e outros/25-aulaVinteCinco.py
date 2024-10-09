
try:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    if nome and idade : #COLOCANDO DIRETO ELE VAI AVALIAR SE CONTEM VALORES
        idade = int(idade)
        print(f"Seu nome é {nome}")
        print(f"Seu nome invertido é {nome[-1::-1]}")

        if " " in nome:
            print("Seu nome contem espaços")
        else:
            print("Seu nome não contem espaços")

        print(f"Seu nome contem {len(nome)} letras")
        print(f"A primeira letra do seu nome é {nome[0]}")
        print(f"A ultima letra do seu nome é {nome[len(nome) - 1]}")
        print(f"A ultima letra do seu nome é {nome[-1]}")
    else:
        print("Desculpe voce deixou campos vazios")

except: #exceção generica
    print("Desculpe voce digitou algo incorreto nos campos, tente novamente")
finally:
    print("fechando")
