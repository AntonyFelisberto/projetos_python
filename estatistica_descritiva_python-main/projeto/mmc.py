import random

T = 9000000

I = 0

for i in range(T):
    x = random.random()
    y = random.random()
    if((x*x) + (y*y) < 1):
        I = I + 1

PI = 4 * I/T