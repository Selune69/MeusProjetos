def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multi(1, 2, 3, 4, 5)
print(multiplicacao)

def par_impar(x):
    if x % 2 == 0:
        return f'{x} e par'
    return f'{x} e impar'

print(par_impar(9))
print(par_impar(4))