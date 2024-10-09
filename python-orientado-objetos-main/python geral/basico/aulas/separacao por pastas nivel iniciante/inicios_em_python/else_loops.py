valor = 12
nums = 22

while valor <= nums // 2:
	print(valor)
	valor+=1

while valor < 10:
	print(valor)
	valor+=1
else:
	print("foi")
	
while valor > 10:
	if valor == 1:
		break
	elif valor >= 100:
		continue
	else:
		pass
	valor-=1
else:
	print("foi")