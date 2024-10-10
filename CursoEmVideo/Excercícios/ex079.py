lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if pergunta == 'N':
        break
print(f'Voce digitou os valores {sorted(lista)}')
