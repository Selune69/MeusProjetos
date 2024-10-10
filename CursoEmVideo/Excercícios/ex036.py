casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos irá pagar? '))

prestação = casa / (anos * 12)
salpor = (sal * 30) / 100

print(f'Para pagar uma casa de R${casa:.2f} por {anos} anos a prestação será de R${prestação:.2f}.')

if prestação > salpor:
    print('\033[41mNEGADO, a prestação excede os 30% do salário.\033[m')
else:
    print('Emprestimo pode ser CONCEDIDO.')
