valor = "my_key"
dicts = {
    "nome":"antony",
    "idade":11,
    "nota":1.1,
    "estado":True,
    valor:"aaa",
    "my_another":["ingles","portuguese"]
}

print(type[dicts])
print(dir(dict))
print(len(dicts))
print(dicts["my_another"][1])
print(dicts.keys())
print(dicts.values())
print(dicts.items())
print(dicts.get("nome"))
print(dicts.get("nome",[]))
print(dicts["nome"])
print(dicts["idade"])
print(dicts["nota"])
print(dicts)

dicts["idade"] = 12
dicts["my_another"].append("arks")
#dicts.pop()         #no dict é esperado um argumento no pop
dicts.pop("nota")
dicts.update({"nota":55.5,"Sexo":"M"})
print(dicts)
del dicts["estado"]
dicts.clear()
