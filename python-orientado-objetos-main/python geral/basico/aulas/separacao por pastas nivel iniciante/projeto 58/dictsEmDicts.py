jogador = dict()
time = list()
partidas = list()

#jogador = times = list() #sempre que voce faz associações assim voce esta associando uma variavel na outra
while True:
    jogador.clear()
    partidas.clear()

    jogador['nome'] = str(input("NOME DO JOGADOR: "))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
    for c in range(0,tot):
        partidas.append(int(input(f"quantos gols na primeira partida {c+1}: ")))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)

    time.append(jogador.copy())
    
    while True:
        resp = str(input("quer continuar S ou N: ")).upper()[0]
        if resp in 'SN':
            break
        print("Erro responda sim ou não")
    if resp == 'N':
        break

for i in jogador.keys():
    print(f'{i:<15}',end='')
print()

for k,v in enumerate(time):
    print(f'{k:>4}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

print(jogador)

for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}')

print(f"o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
for i,v in enumerate(jogador['gols']):
    print(f"na partida {i+1} fez {v} gols")

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para sair): "))
    if busca == 999:
        break
    if busca >= len(time):
        print("jogador não existe")
    else:
        print(f'JOGADOR {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('-'*40)