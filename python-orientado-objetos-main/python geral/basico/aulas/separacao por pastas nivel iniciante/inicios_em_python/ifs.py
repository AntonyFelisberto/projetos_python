#temperaturas - cozimento

tem_cel = int(input("QUAL A TEMPERATURA: "))

if tem_cel < 48:
	print("cozinha mais")
elif tem_cel in range(48,53):
	print("selada")
elif tem_cel in range(54,59):
	print("ao ponto para o mal")
elif tem_cel in range(60,64):
	print("ao ponto")
elif tem_cel in range(65,70):
	print("ao ponto para o bem")
else:
	print("Bem passado")
	
verdade = True
nome = ""
idade = 11
somar = 12
items = False
ads = 11

if verdade:
	if (nome == "ads") and (idade > 15 or idade == 10) and not(somar == 10 and items!=False):
		pass
	elif ads == 11:
		pass
	else:
		pass