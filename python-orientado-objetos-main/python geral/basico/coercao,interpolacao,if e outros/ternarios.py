lockdown = True
valor = 400

status = "Casa" if lockdown or valor <= 400 else "Fora"
status_out = "Casa" if lockdown and valor <= 400 else "Fora"
print(f'{status}')