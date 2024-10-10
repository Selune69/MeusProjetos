quantia_litros = int(input('Quantos litros voce deseja abastecer? '))
tipo = input('''Qual tipo de combustivel voce deseja? 
A - Alcool
G - Gasolina
''')
alcool = quantia_litros * 1.90
gasolina = quantia_litros * 2.50

if tipo in 'Aa':
    preco = alcool
    desconto1 = 0.03
    desconto2 = 0.05
elif tipo in 'Gg':
    preco = gasolina
    desconto1 = 0.04
    desconto2 = 0.06
if quantia_litros <= 20:
    valor = preco - (preco * desconto1)
else:
    valor = preco - (preco * desconto2)
print(f'O valor quer voce ira pagar e RR${valor:.2f}')