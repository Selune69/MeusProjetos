lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

for i, numero in enumerate(lista):
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append(numero)

print(f'A lista completa e {lista}')
print(f'A lista de pares {pares}')
print(f'A lista de impares {impares}')