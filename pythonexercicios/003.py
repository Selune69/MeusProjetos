quant_morangos = float(input('Quantos Kg de morango? '))
quant_macas = float(input('Quantos Kg de maca? '))

preco_morangos = preco_macas = preco_total = 0
preco_morangos1 = 3.5
preco_morangos2 = 3.2
preco_maca1 = 2.8
preco_maca2 = 2.5

peso_total = quant_morangos + quant_macas

if quant_morangos <= 5:
    preco_morangos = preco_morangos1 * quant_morangos
else:
    preco_morangos = preco_morangos2 * quant_morangos

if quant_macas <= 5:
    preco_macas = preco_maca1 * quant_macas
else:
    preco_macas = preco_maca2 * quant_macas

preco_total = preco_macas + preco_morangos

if peso_total > 8 or preco_total > 25:
    desconto = peso_total * 10 / 100
    preco_total = peso_total - desconto
    print(f'O preco final e {preco_total:.2f} com o desconto de {desconto:.2f}')
else:
    print(f'O preco final e {preco_total:.2f}')