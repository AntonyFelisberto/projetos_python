def soma(a,b):
    return a + b

def functional(funcao,a,b):
    return funcao(a,b)

print(functional(soma,12,33))

def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma

funcao_parcial_soma = soma_parcial(10)
funcao_final = funcao_parcial_soma(10)
print(funcao_final)
funcao_total = soma_parcial(10)(20)
print(funcao_total)