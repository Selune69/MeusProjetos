n = int(input('Digite um numero: '))
for x in range(1, n+1):
    print(end='\n')
    for y in range(1, n+1):
        if x >= y:
            print(x, end='')