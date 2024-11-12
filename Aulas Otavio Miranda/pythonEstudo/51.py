def nao_aceito_zero(y):
    if y == 0:
        raise ZeroDivisionError('Nao e possivel a divisao por zero.')
    return True

def int_ou_float(x):
    if not isinstance(x, (float,int)):
        raise TypeError(
            f'{x} deve ser int ou float.'
        )
    return True
def divide(x, y):
    int_ou_float(x)
    nao_aceito_zero(y)
    return x / y

print(divide(8, 0))