s = 0

for c in range (1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 1:
        s = s
    else:
        s = s + n

print(s)