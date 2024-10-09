def itens(args):
    if len(args) == 7:
        return True
    else:
        return False

if itens({1,2,3,4,5,6,7}):
    print(True)
