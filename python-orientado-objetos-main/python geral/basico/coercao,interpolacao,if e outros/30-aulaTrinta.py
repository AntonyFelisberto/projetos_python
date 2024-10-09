#TIPOS IMUTAVEIS str,int,float,bool TODOS SÃO OBJETOS, O QUE SIGNIFICA QUE CADA UM TEM MÉTODOS DENTRO DELES

atributo = "abcdefgh"
outra_variavel = f'{atributo[:3]}ABC{atributo[4:]}'
#atributo[3] = "123" #vai dar erro pois a variavel não pode ser alterada
print(atributo.capitalize())
print(atributo.zfill(1000))