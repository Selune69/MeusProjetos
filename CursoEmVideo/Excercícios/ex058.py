from random import randint
computador = randint(0, 2)

print('Sou o seu computador...')
print('Acabei de pensar em um número entre 0 a 10. Você consegue adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        else:
            print('Menos... tente mais uma vez.')

print(f'''Parabéns! o número que pensei é {computador}. Você ganhou!
 Você precisou de {palpites} palpites para acertar''')