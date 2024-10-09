def saudar(nome="Pessoa",idade=20):
    print(f"Bom dia {nome} vc tem {idade} anos")

def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

def results(**args):
    print(type(args))
    status = "aprovado" if args["nome"] == "antony" else "reprovado"
    print(f"{status}")

saudar(idade=40)
saudar("antony",39)
soma(1,2,4,5,8,7,8,4,4,7,5)
results(nome="antony",nota=4.7)
