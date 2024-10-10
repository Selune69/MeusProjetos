a = (int(input('Digite o primeiro numero: ')),
    int(input('Digite o primeiro numero: ')),
    int(input('Digite o primeiro numero: ')),
    int(input('Digite o primeiro numero: ')))
print(f'Voce digitou os valores {a}')
print(f'O valor 9 apareceu {a.count(9)} vezes.')
if 3 in a:
    print(f'O valor 3 apareceu na {a.index(3) + 1} posicao.')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao.')
print('O valores pares sao:')
for n in a:
    if n % 2 == 0:
        print(n, end='')