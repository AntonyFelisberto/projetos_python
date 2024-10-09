print({1,2,3,4})
print(type({1,2,3,4}))

sets = {1,2,3,4}
print(sets)
#print(sets[0]) #da erro pois não da pra acessar posições
print({1,2,3,4,5,6,5})

a = set("aaaaa")
print(a)
print("a" in a,"b" not in a)
print({1,2,3}=={3,2,1,3})

c_um = {1,2,3}
c_dois = {4,5,2}
print(c_um.union(c_dois))
print(c_um.intersection(c_dois))
print(c_um.update(c_dois),c_um,c_dois)
print(c_um >= c_dois, c_um <= c_dois)
print({1,2,3}-{2})
print(c_dois-c_um)
c_um-={2}
print(c_um)