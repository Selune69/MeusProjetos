from random import randint
print('Vamos jogar Par ou Impar')
print('-' * 30)

cont = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint (1, 10)
    aposta = ' '
    
    while aposta not in 'PI':
        aposta = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    Total = jogador + computador
    print(f'Voce jogou {jogador} e o computador {computador}. Total deu {Total}.')
    
    if Total % 2 == 0:
        if aposta == 'P':
            print('Voce Venceu! Vamos jogar novamente...')
            cont = cont + 1
        elif aposta == 'I':
            print('Voce PERDEU!!')
            break
    elif Total % 2 == 1:
        if aposta == 'I':
            print('Voce Venceu! Vamos jogar novamente...')
            cont = cont + 1
        elif aposta == 'P':
            print('Voce PERDEU!')
            break
    print('Vamos jogar novamente...')

print(f'GAME OVER! Voce venceu {cont} vezes.')