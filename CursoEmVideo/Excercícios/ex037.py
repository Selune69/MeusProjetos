n = int(input('Digite um número para converter: '))

print('''Escolhar uma das bases para a conversão:
[ 1 ] para converter para BINÁRIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{bin(n)[2:]}')
elif opção == 2:
    print(f'{oct(n)[2:]}')
elif opção == 3:
    print(f'{hex(n)[2:]}')
    