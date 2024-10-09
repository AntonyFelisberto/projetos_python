#para começar com cores voce coloca \033[m  , entre o [ e o m vice coloca o estilo
#\033[0;33;44m
#\033[style;text;back m
#tudo é opcional o padrão é \033[m
#quando coloca só 2 itens significa o text e o back \033[30;40m

#style 0 none 1 bold 4 underline 7 negative
#text vai de 30 até 37
#back vai de 40 até 47
print("\033[mOla mundo")
print("\033[31mOla mundo")
print("\033[31;43mOla mundo")
print("\033[1;31;43mOla mundo")
print("\033[1;31;43mOla mundo\033[m") #esse \033[m é pra tirar a formatação no final
print("\033[4;30;45mOla mundo\033[m") 
print("\033[30mOla mundo\033[m") 
print("\033[7;30mOla mundo\033[m")      #o 7 inverte a cor do text com a cor do back
print("\033[0;33;44mOla mundo\033[m") 
print("\033[7;33;44mOla mundo\033[m") 
a = 5
b = 8
print(f"valores são \033[32m{a=} \033[31m{b=}")
print(f"valores são \033[32;44m{a=} \033[31;44m{b=}\033[m")
print("código de cor é {}{}{}".format('\033[1;34m',a,'\033[m'))
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'preto_branco':'\033[7;30m'
}
print("código de cor é {}{}{}".format(cores['azul'],a,cores['limpa']))