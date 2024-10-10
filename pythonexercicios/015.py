numero = int(input('Digite um numero: '))
total = 0
for cada in range(1, numero + 1):
    print(cada)
    total += cada

print(f'Total: {total}')