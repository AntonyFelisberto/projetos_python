print(__package__)

a = 10
b = 30

a,b = b,a
print()

diferente = a != b
negado = not a
negado_negado = not not a

#USADO PARA COMPARAR BITS - ESSE TEM PRIORIDADE AOS OUTROS
operador_bit_um = True & False      #and
operador_bit_dois = True | False    #or
operador_bit_tres = True ^ False    #not

verdade="ate"
falco = 0
verdade = -0.22
falco = ""
verdade = ' '
falco = []
falco = {}

condicional_inline = True if input("Y OR N") == "Y" else False

try:
    print(int("aaaaaaa"))
except:
    print("erro")