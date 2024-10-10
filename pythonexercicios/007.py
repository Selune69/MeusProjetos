n = int(input('Digite um numero: '))
for linha in range(1, n+1):
    print(linha, end='\n')
    if linha == n:
        break
    for coluna in range(1, n+1):
        if linha >= coluna:
            print(coluna, end='')