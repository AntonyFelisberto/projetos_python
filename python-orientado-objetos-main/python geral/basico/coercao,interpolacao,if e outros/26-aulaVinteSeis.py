#EM PYTHON O TRATAMENTO DE EXCEÇÃO É COM TRY E EXCEPT
try:
    print(input("digite um numero").isdigit)
    int('a')
    print(1 + "aaa")
    ...     #serve para dizer que ainda vai adicionar código
    pass    #serve para dizer que ainda vai adicionar código
except:
    print("deu erro")
finally:
    print("erro fechado")

a = input("digite algo")
if(a.isdigit()):
    numero = int(a)
    print("foi convertido")
else:
    print("não é um numero")