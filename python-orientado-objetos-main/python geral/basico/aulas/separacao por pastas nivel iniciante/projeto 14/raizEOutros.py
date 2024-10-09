n = int(input('digite um numero :'))
d = n * 2
t = n* 3
r = n ** (1/2)
print('o dobro de {} vale {}'.format(n,d))
print('o triplo de {} vale {} e a raiz vale {:.2f} \n usando pow a raiz fica {:.2f}'.format(n,t,r, pow(n,(1/2))))
