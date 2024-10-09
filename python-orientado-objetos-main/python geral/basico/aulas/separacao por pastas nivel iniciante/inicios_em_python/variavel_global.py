def numeros():
	variavel=10
	print(variavel)

variavel=20
print(variavel)
print(numeros())

def numeros():
	global variavel
	variavel=10
	print(variavel)


print(variavel)
print(numeros())

def multiplos(args, *vart):
	print(args)
	for item in vart:
		print(item)