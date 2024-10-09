print(dir(str))
nome = "aaaa em bbb"
print(nome[0])
print(nome[2:4])
print(nome[-5:])
print(nome[:4])
print(nome[::])
print(nome[::2])
print(nome[::-1])
print(nome[::-2])
print(nome[1::2])
#nome[0] = "a" #vai dar erro pois a variavel é imutavel
docs = """ minha doc \t \n 'aspas' """
print("aa" in nome)
print(nome.split(" "))
print(help(str.center))

a = "aaa"
b = "asd"
print(a+b)
print(a.__add__(b)) #metodos qie possuem o __nome__ são chamados de metodos magicos
print(str.__add__(a,b))
print(a.__len__())
print("a" in nome)  #isso seria a mesma coisa do __contains__
print(a.__contains__("a"))