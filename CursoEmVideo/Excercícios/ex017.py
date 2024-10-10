from math import sqrt
CatetoO = float(input('Qual é o valor do cateto oposto? '))
CatetoA = float(input('Qual o valor do cateto adjacente? '))

h = CatetoO ** 2 + CatetoA ** 2

print(f'A hipotenusa é igual à {sqrt(h):.2f}')
