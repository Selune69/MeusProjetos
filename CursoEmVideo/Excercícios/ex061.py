print('-=' * 20)

n1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZAO DA PA: '))

termo = n1
c = 1

while c <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    c = c + 1
