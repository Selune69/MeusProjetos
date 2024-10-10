from random import randint
from time import sleep

computador = randint(0, 5) #Faz o computador PENSAR

print('-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
print('-' * 30)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Você errou. Eu pensei no número {computador}')
