sal = float(input('Qual o salário de um funcionário? R$'))

sal1 = (sal * 15 / 100) + sal
sal2 = (sal * 10 / 100) + sal

if sal <= 1250:
   print(f'O funcionário que ganhava R${sal} passará a receber R${sal1:.2f}.')
else:
    print(f'O funcionário que ganhava R${sal} passará a receber R${sal2:.2f}.')
