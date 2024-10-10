print('-' * 20)
print('10 TERMOS DE UMA PA')
print('-' * 20)

p1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

déc = p1 + (10 - 1) * r

for c in range (p1, déc + r, r):
    print(c,end=' -> ')

print('Acabou!!')
