#if/elif/else
entrada = input("voce quer entrar ou sair ? ")

if entrada == "entrar": #NO PYTHON SE USA : PARA DIZER O FIM DO IF/ELSE/ELIF
    print("ENTRANDO")              #EM PYTHON A IDENTAÇÃO É IMPORTANTE POIS É ELA O QUE DIZ O QUE ESTA EXECUTANDO O QUE
elif entrada == "sair":
    print("SAINDO")
elif entrada == "":
    print("voce não digitou nada")
else:
    print("OPÇÃO NÃO ENTENDIDA")
