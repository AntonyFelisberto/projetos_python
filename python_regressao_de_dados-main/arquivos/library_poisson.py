from scipy.stats import poisson
from math import pow,factorial

def poissons(x,lam):
    return pow(2.71828,-lam) * pow(lam,x) / factorial(x)

print(poissons(3,2))
print(poisson.pmf(3,2))