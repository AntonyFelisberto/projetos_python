import time

def abre_arquivo():
    try:
        open("arquivo.txt")
        return True
    except:
        print("erro")
        return False

try:
    while not abre_arquivo():
        print("tentando abrir arquivo")
        time.sleep(5)
    print(1/0)
except ZeroDivisionError as error:
    print("error",error.__cause__)
except RecursionError:
    print("error")
    time.sleep(5)
    abre_arquivo()
except:
    print("erro generico")
