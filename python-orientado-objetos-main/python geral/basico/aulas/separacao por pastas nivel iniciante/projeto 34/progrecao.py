from time import sleep
print("PAS")
print("-="*10)
primeiro = int(input("primeiro termo: "))
razao = int(input("razão da Pa: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} ->",end='')
        termo += razao
        cont += 1
    sleep(0.5)
    print(" FIM")
    mais = int(input("quantos termos a mais: "))
print("Fim")