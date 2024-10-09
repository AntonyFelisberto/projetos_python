def calculo_base(numero,base):
    binario = ''
    while numero > 0:
        binario += str(numero% base)
        numero = int(numero /  base)
    return binario[::-1]

def calculo_binario_para_decimal(binario):
    numero_contagem = -1
    numero_convertido = 0
    for i in binario[::-1]:
        if int(i) == 0:
            numero_contagem = numero_contagem + numero_contagem if numero_contagem >= 1 else 1
        if int(i) == 1:
            numero_contagem = numero_contagem + numero_contagem if numero_contagem >= 1 else 1
            numero_convertido = numero_contagem + numero_convertido
    print(numero_convertido)

print(f"BASE OCTAL {calculo_base(1264,8)}")
print(f"BASE BINARIO {calculo_base(1264,2)}")
binario = calculo_base(25,2)
calculo_binario_para_decimal(binario)