def potencia(x):
    return x ** 2

def fahrenheit(t):
    return ((float(9)/5)*t + 32)

def celsius(t):
    return ((float(5)/9)*t - 32)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numero_ao_quadrado = list(map(potencia,numeros))

temperaturas = [0,22.5,40,100]

print(map(fahrenheit,temperaturas))
print(list(map(fahrenheit,temperaturas)))

for item in map(fahrenheit,temperaturas):
    print(item)

print(map(celsius,temperaturas))
print(list(map(celsius,temperaturas)))

for item in map(celsius,temperaturas):
    print(item)

print(map(lambda x: (5.0/9)*(x - 32),temperaturas))
print(list(map(lambda x: (5.0/9)*(x-32),temperaturas)))
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
print(list(map(lambda x,y:x+y,a,b)))
print(list(map(lambda x,y,z: x + y + z,a,b,c)))
