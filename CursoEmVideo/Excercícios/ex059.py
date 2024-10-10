import time
from time import sleep
opção = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opção != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS 
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('>>>>>>>>>>> Qual é a sua opção: '))
    if opção == 1:
        print(f'O resultado de {n1} + {n2} é igual a {n1 + n2}.')
    elif opção == 2:
        print(f'O resultado de {n1} X {n2} é igual a {n1 * n2}.')
    elif opção == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior número é {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior número é {n2}')
        else:
            print(f'Entre {n1} e {n2} os dois possuem o mesmo valor.')
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
        print('=-' * 20)
        print('Fim do programa! Volte sempre.')
    else:
        print('Opção inválida. Tente novamente. ')