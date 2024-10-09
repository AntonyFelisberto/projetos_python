def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
valores = [1,2,3,4,5,6,78]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s+= num
        print(s,end='',flush=True)
soma(1,21,3,1,4,2)

def fatorial(n,show=False):
    """
        -> calcular fatorial
        :param n: o numero a ser calculado
        :param show: opcional mostrar ou não a conta
        :return o valor do fatorial de um numero n
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print(' X ',end='')
            else:
                print(' = ',end='')
        f *=c
    return f
help(fatorial)
print(fatorial(5))
print(fatorial(5,show=True))
print(fatorial(5,True))

def ficha(jogo='desconhecido',gol=0):
    print(f'O jogador {jogo} fez {gol} no campeonato')
n=str(input("nome jogador: "))
g=str(input("numero de gols: "))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)

def somas(param_um,param_dois):
    return param_um + param_dois
print(somas(1,2))

def leia_int(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO, VALOR NÃO NUMERICO\033[m")
        if ok:
            break
    return valor

n = leia_int('Digite um numero: ')
print(f"voce digitou o numero {n}")

