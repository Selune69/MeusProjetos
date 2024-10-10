n = int(input('Digite um número: '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        tot = tot + 1
    else:
        print('\033[m', end=' ')
    print(c)
print(f'O número foi divísivel {tot} vezes')
if tot > 2:
    print('O número NÃO é um número PRIMO.')
else:
    print('O número é um número PRIMO.')
