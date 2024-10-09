#EXERCICIOS ENUNCIADOS
entrada = input("digite um numero ")
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0

    par_impar_texto = "impar"
    if par_impar:
        par_impar_texto = "par"

    print(f"o numero {entrada} é {par_impar_texto}")
else:
    print("numero não inteiro")