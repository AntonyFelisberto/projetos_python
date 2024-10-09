listas = [1,1.2,True,"Artorias"]

listas = [1,2,3,4,5,6,7,8,9]
for i in range(0,len(listas)):
	print(listas[i])
	
	
for i in range(0,20,-2):
	print(i)
	

funcionarios = ["ana","marcos","alice","pedro","sophia","bruno","meissa"]
turno_dia = ["ana","marcos","alice","melissa"]
turno_noite = ["pedro","sophia","bruno"]
tem_carro = ["marcos","alice","bruno","melissa"]

lista = set(tem_carro).intersection(turno_noite)
print(lista)

lista_dois = set(tem_carro).intersection(turno_dia)
print(lista_dois)

lista_tres = lista_dois = set(funcionarios).difference(tem_carro) #vai pegar quem não tem carro
print(lista_tres)

del lista_dois[0]

listas_aninhadas = [[1,2,3][4,5,6][10.9,8,7]]
listas_aninhadas[0]
listas_aninhadas[0][1]

lista_um=[1,2,3,-1,-3.5]
lista_dois=[4,5,6]
lista_tres=lista_um+lista_dois
print(10 in lista_tres)

type(lista_um)
lista_um.append(10)
lista_um.count(100)
help(lista_um)
dir(lista_um)