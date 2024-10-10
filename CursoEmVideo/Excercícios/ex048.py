s = 0
count = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        s = s + c
        count = count + 1

print(f'A soma de todos os valores solicitados é {s}.')
print(f'No total foram {count} números ímpares divisíveis por 3.')