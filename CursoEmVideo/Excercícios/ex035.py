print('-' * 30)
print('\033[32mAnalisador de triângulos\033[m')
print('-' * 30)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Parabéns, você pode formar um triângulo')
else:
    print('Não é possivel formar um triângulo')
