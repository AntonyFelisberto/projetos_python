jogador = dict()
partidas = list()
jogador['nome'] = str(input("NOME DO JOGADOR: "))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))

for c in range(0,tot):
    partidas.append(int(input(f"quantos gols na primeira partida {c}: ")))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)

print(jogador)
for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}')

print(f"o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for i,v in enumerate(jogador['gols']):
    print(f"na partida {i+1} fez {v} gols")