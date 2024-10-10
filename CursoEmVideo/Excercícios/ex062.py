print('-=' * 20)

n1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZAO DA PA: '))

termo = n1
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        c = c + 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
