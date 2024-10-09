#EXERCICIOS ENUNCIADOS

entrada = input("digite seu nome ")
tamanho = len(entrada)

if tamanho > 1:
    if tamanho <=4:
        print("seu nome é curto")
    elif tamanho >=5 and tamanho <= 6:
        print("seu nome é normal")
    else:
        print("seu nome é grande")
else:
    print("digite mais de uma letra")
