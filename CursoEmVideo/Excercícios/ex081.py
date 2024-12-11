lista = []
c = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break

print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print(f'O valor 5 aparece na lista')