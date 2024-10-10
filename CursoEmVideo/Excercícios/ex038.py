n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('Processando...')

if n1 > n2:
    print('O primeiro valor é MAIOR.')
elif n2 > n1:
    print('O segundo valor é MAIOR.')
elif n1 == n2:
    print('Os dois números possuem o MESMO valor.')
