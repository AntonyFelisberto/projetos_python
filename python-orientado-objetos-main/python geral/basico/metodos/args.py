import sys

args = sys.argv
print(args)

def soma(n_um,n_dois):
    return n_um + n_dois

if args[1] == "soma":
    soma = soma(args[2],args[3])
