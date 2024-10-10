from datetime import date
nasc = int(input('Que ano nasceu: '))

ano_atual = date.today().year
idade = ano_atual - nasc

print(f'Você tem {idade} anos')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
