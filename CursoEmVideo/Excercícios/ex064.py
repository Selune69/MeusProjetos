n = 0
c = 0
s = 0

while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        c = c + 1
        s = s + n

print(f'Voce digitou {c} numeros e a soma entre eles foi {s}')
print('Acabou')
