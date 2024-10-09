help(input)
print(input.__doc__)

def todos_opcional(a=0,b=0,c=0):
    s = a+b+c
    print(s)
todos_opcional(1,2,3)
todos_opcional(1,2)
todos_opcional(1)
todos_opcional()
todos_opcional(a=1,c=2,b=11)

def escopo_variavel():
    x = 8
    print(f'o valor de x é {x}')
escopo_variavel()
try:
    print(f'o valor de x é {x}')
except:
    print('x não existe')

def testes(b):
    a=10 #a local, não é o mesmo do outro a global
    b+=4
    print(f'o A local vale {a}')
a=5 #a global
testes(a)
print(f'o A global vale {a}')

def testes_globais(b):
    global a
    a=10 #a local, não é o mesmo do outro a global
    b+=4
    print(f'o A local vale {a}')
a=5 #a global
testes_globais(a)
print(f'o A global vale {a}')

def retorna():
    return "abc"
print(retorna())

def notas(*notas,sit=False):
    r= dict()
    r['total']=len(notas)
    r['maior']=max(notas)
    r['menor']=min(notas)
    r['media']=sum(notas)/len(notas)
    if sit:
        if r['media'] >=7:
            r['situação']='BOA'
        elif r['media'] >=5:
            r['situação']='Razoavel'
        else:
            r['situação']='Ruim'
    return r
resp = notas(50,55,44)
print(resp)
resp = notas(50,55,44,sit=True)
print(resp)

from time import sleep
def contador(i,f,p):
    """
        programa para contador
        i -> inicio
        f -> fim
        p -> passo
    """
    if p < 0:
        p*=-1
    if p==0:
        p=1

    if i < f:
        cont = i
        while cont<=f:
            print(f'{cont}',end=' ',flush=True) #flush não vai pausar a tela
            sleep(0.5)
            cont+=p
    else:
        cont = i
        while cont>=f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont-=p

contador(10,50,5)
help(contador)
contador(int(input("digite o inicio: ")),int(input("digite o fim: ")),int(input("digite o passo: ")))

