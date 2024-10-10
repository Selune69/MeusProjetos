vel = float(input('Qual a velocidade do seu carro? '))

print('Tenha um bom dia.')

if vel > 80:
    multa = (vel - 80) * 7
    print('Você excedeu o limite permitido de 80km/h')
    print(f'Você deve paga um multa de R${multa}')