def recursivo(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * recursivo(n-1)
		
print(recursivo(11))

