n = int(input('Digite um número: '))

c = n
f = 1

while c > 0:
    print(c, ' X ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1

print(f)
