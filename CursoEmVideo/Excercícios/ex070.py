print('-' * 30)
print('LOJA SUPER BARATAO')
print('-' * 30)

total = contP = barato = cont = 0

while True:
    prod = str(input('Nome do Produto: '))
    valor = float(input('Preco: '))
    cont = cont + 1
    total = total + valor
    
    if valor > 1000:
        contP = contP + 1
    if cont == 1:
        barato = valor
    else:
        if barato < valor:
            valor = barato
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('--------- FIM DO PROGRAMA ---------')
print(f'''O total da compra foi R${total}
Temos {contP} produtos custando mais de 1000
O produto mais barato custa {barato}''')