try:
    n_um = int(input("numero: "))
    n_dois = int(input("numero: "))
    r = n_um/n_dois
except (ValueError,TypeError):
    print('erro especifico')
except Exception as erro: # um try pode ter varios excepts 
    print(f"erro ocorrido foi {erro.__class__}")
    print(f"erro ocorrido foi {erro.__cause__}")
except KeyboardInterrupt:
    print('não informou dados')
except:
    print("erro ocorrido")
else:
    print(f"o resultado foi {r:.1f}")
finally:
    print("programa finalizado")