n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.1f}')
if m >= 7:
    print('Uau, parabéns!!! Você passou de ano')
else:
    print('Que decepção. Você reprovou.')
