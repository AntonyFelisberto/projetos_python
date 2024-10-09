from time import sleep

num = int(input("digite um numero"))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m',end='')    #\033[34 mudando a cor do terminal
    else:
        print('\033[31m',end='')

for i in range(0,11):
    print(i)

for i in range(2,51,2):
    if i % 2 == 0:
        print(i,end=' ')

for i in range(10,-1,-1):
    print(i)
    sleep(0.5)

inicio = int(input("inicio: "))
fim = int(input("fim: "))
passo = int(input("passo: "))
for i in (inicio,fim+1,passo):  #fim + 1 pois ele sempre faz do inicio até -1
    print(i)
