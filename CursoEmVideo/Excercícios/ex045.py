from random import randint
from time import sleep

print('SUAS OPÇÕES: ')

itens = ('pedra', 'papel', 'tesoura')
computador = randint (0, 2)

print('''ESCOLHA ENTRE
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')

opção = int(input('QUAL A SUA JOGADA? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-' * 20)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[opção]}')
print('-' * 20)

if computador == 0:
    if opção == 0:
        print('EMPATE')
    elif opção == 1:
        print('VOCÊ VENCEU')
    elif opção == 2:
        print('VOCÊ PERDEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 1:
    if opção == 0:
        print('VOCÊ PERDEU')
    elif opção == 1:
        print('EMPATE')
    elif opção == 2:
        print('VOCÊ VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 2:
    if opção == 0:
        print('VOCÊ VENCEU')
    elif opção == 1:
        print('VOCÊ PERDEU')
    elif opção == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')
