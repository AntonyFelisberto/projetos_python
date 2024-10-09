#EXERCICIOS ENUNCIADOS

entrada = input("digite a hora em numeros inteiros: ")
try:
    hora = int(entrada)

    if hora >= 0 and hora <=11:
        print("good morning")
    elif hora >= 12 and hora <= 17:
        print("good afternoon")
    elif hora >= 18 and hora <= 23:
        print("good evening")
    else:
        print("hora não conhecida")
except:
    print("digite um numero inteiro")