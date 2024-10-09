"""
Interpolação basica de strings

%s      - STR
%d e %i - INT
%f      - FLOAT
x e X   - HEXADECIMAL (ABCDEF0123456789)
"""
nome = "Antony"
preco = 157.89
variavel_de_interpolacao_um = "%s, o valor deu 0" %nome         #QUANDO VOCE USA SÓ UM VALOR NÃO PRECISA DO ()
variavel_de_interpolacao = "%s, o valor deu R$%.2f" %(nome,preco)   #QUANDO VOCE USA MAIS DE UM VALOR PRECISA DO ()
print(variavel_de_interpolacao)
print("%s, o valor deu R$%.2f" %(nome,preco))
print("%s, apresentando o hexadecimal de %d sendo ele %x "%(nome,19,19))
print("%s, apresentando o hexadecimal de %d sendo ele %04x "%(nome,19,19)) # %0 NUMERO DE CASAS QUE VAI PREENCHER COM 0
print("%s, apresentando o hexadecimal de %d sendo ele %08X "%(nome,19,19)) 