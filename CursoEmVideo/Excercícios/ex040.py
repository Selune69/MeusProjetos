n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2

print(f'Você tirou na média {m:.1f}')

if m >= 7:
    print('Parabéns!! Você passou de ano.')
elif m < 7 and m >= 5:
    print('Que pena! Você ficou de recuperação.')
elif m < 5:
    print('Você REPROVOU!')
