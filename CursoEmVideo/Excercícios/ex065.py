p = ''
c = 0
s = 0
media = 0
maior = 0
menor = 0
n = 0

while p in 'Ss':
    n = int(input('Digite um numero: '))
    p = str(input('Quer continuar? [S/N] ')).upper().strip()
    c = c + 1
    s = s + n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = s / c

print(f'Voce digitou {c} numeros e a media foi {media:.1f}')
print(f'O maior valor digitado foi o {maior} e o menor foi {menor}')
