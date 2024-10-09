"""
FORMATAÇÃO DE STRINGS
s - str
d - int
f - float

PREENCHIMETOS 

variavel:LADO DE PREENCHIMENTO QUANTIDADE
> - Esquerda
< - Direita
^ - Centro

"""
variavel = "ABC"
print(f"{variavel}")
print(f"{variavel:<10}.")
print(f"{variavel:^10}.") #NO CENTRO DIVIDE OS NUMEROS DE CARACTERES DOS DOIS LADOS
print(f"{variavel:Z^10}.")#DA PRA ANTES DO LADO DE PREENCHIMENTO COLOCAR COM O QUE VOCE QUER QUE PREENCHA
print(f"{1000.90:.2f}")
print(f"{1000.90:,.2f}")#DA PRA ANTES DO LADO DE FORMATAÇÃO COLOCAR COM O QUE VOCE QUER QUE PREENCHA A CASA DECIMAL
print(f"{-1000.90:.2f}")
print(f"{1000.90:+.2f}")#DA PRA COLOCAR O SINAL DE + OU DE - PRA APARECER QUANDO O NUMERO FOR POSITIVO OU NEGATIVO
print(f"{-1000.90:-.2f}")#PARA NEGATIVOS POR PADRÃO ELE MOSTRA O -

#DA PARA COLOCAR O NUMERO QUE VOCE QUER QUE APAREÇA EM QUAL POSIÇÃO E O NUMERO DE VEZES, 
#FICANDO numero posição sinal numeroDeVezesQueVaiAparecer
#POREM NESSE CASO O SINAL FICA APÓS O NUMERO INSERIDO
print(f"{-1000.90:0>-10,.2f}")

#AI PRA FORÇAR O SINAL A APARECER ANTES DE TUDO É USADO O =
print(f"{-1000.90:0=-10,.2f}")

#MOSTRANDO HEXADECIMAL
print(f"O HEXADECIMAL É {1500:08X}")

#CONVERTION FLAGS
# !r chama o métod __repr__
# !s chama o método __str__
# !a chama o método __asc__
print(f'{variavel!r}')
