maior = 0
menor = 0

for pessoa in range (1, 6):
    peso = float(input(f'Peso da pessoa {pessoa}º: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso lido foi o de {maior}kg.')
print(f'O menor peso lido foi o de {menor}kg.')
