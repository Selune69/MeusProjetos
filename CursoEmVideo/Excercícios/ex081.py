lista = []
c = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if pergunta in 'N':
        break
    if lista in 'S':
        c = c + 1
#print(f'Voce digitou {len(lista[n])} elementos')
print(f'Os valores em ordem decrescente sao {lista.sort(reverse=True)}')
print(f'O valor 5 aparece {c} vezes')