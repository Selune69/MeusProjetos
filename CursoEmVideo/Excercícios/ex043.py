peso = float(input('Qual o peso? '))
altura = float(input('Qual a altura? '))
imc = peso / altura ** 2
print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
