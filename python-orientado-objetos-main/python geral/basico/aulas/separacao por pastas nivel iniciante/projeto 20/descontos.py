preco = float(input('Qual é o preço do produto ? '))
novo = preco - (preco * 5/ 100)
print('custava {:.2f} com desconto de 5% vai ficar {:.2f}'.format(preco,novo))