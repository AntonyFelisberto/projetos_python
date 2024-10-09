def prints(val):
    print(val)

def dados(model='dado',real=7.55):
    print(f'{model} {real}')

def is_or_not(value=None):
    print(value if not None else 'None')

def recolocar(valor=''):
    prints(valor.replace(',','.'))
    dados(valor.replace(',','.'))