print(f'\033[42m{" LOJAS LANIER ":=^40}\033[m')
preço = float(input('Preço do produto: R$'))
print('''[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] EM ATÉ 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opção = int(input('ESCOLHA SUA OPÇÃO: '))
if opção == 1:
    VDinheiro = preço - (preço * 10) / 100
    print(f'O valor à vista em dinheiro/cheque do produto ficará R${VDinheiro:.2f}')
elif opção == 2:
    VCartão = preço - (preço * 5) / 100
    print(f'O valor à vista no cartão do produto ficará R${VCartão:.2f}')
elif opção == 3:
    print(f'O valor em até 2x do produto ficará R${preço / 2:.2f} do total de {preço:.2f}')
elif opção == 4:
    meses = int(input('Em quantas parcelas? '))
    Cartão3x = preço + (preço * 20) / 100
    parcela = Cartão3x / meses
    print(f'O valor produto ficará no total com JUROS R${Cartão3x:.2f} e R${parcela:.2f} para serem pagos no periodo de {meses} meses')
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO')
    