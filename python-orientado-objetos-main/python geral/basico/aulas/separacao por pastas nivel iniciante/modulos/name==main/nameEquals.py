from modulo import soma #quando o modulo é importado o nome que vai aparecer no __name__ não é mais __main__ e sim o nome do arquivo

print(__name__) #quando executado o código na própria classe ele exibe main, mas quando ele executa em outro arquivo vai exibir o nome do arquivo

if __name__ == '__main__':
    print(soma(10,30))