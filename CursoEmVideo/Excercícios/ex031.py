di = float(input('Qual a distância da viagem? '))

di1 = di * 0.50
di2 = di * 0.45

if di <= 200:
    print(f'Considerando a distância de {di}km, o valor da passagem será de R${di1:.2f}')
else:
    print(f'Considerando a distância de {di}km, o valor da passagem será de R${di2:.2f}')
    