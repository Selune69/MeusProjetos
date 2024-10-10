l1 = float(input('Primeiro Lado: '))
l2 = float(input('Segundo Lado: '))
l3 = float(input('Terceiro Lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('É possível formar um triângulo')
    if l1 == l2 == l3:
        print('EQUILATERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISOCELES!')
else:
    print('Não é possível formar um triângulo.')
