from string import Template

nome, idade,money = "antony",30,77.7
print("nome %s idade %d money %f %r %s %d"%(nome,idade,money,True,True,True))
print("nome {0} idade {1}".format(nome,idade))
print(f"nome {nome} idade {idade} {2+3+55}")
s = Template("nome $n idade $idade")
print(s.substitute(n=nome,idade=idade))