from random import randint
itens = ["tesoura","papel","pedra"]
computador = randint(0,2)
jogador = int(input("escolha 0 pedra 1 papel e 2 tesoura: "))
if  jogador != computador :
    if (jogador == 0 and computador == 1) or (jogador == 1 and computador == 0):
        if jogador == 0:
            print(f"player ganhou: computador {computador} jogador {jogador}")
        else:
            print(f"computador ganhou: computador {computador} jogador {jogador}")

    if (jogador == 1 and computador == 2) or (jogador == 2 and computador == 1):
        if jogador == 1:
            print(f"player ganhou: computador {computador} jogador {jogador}")
        else:
            print(f"computador ganhou: computador {computador} jogador {jogador}")

    if (jogador == 2 and computador == 0) or (jogador == 0 and computador == 2):
        if jogador == 2:
            print(f"player ganhou: computador {computador} jogador {jogador}")
        else:
            print(f"computador ganhou: computador {computador} jogador {jogador}")
else:
    print("empate")

