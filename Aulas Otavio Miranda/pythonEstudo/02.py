numero = input('Digite um numero inteiro: ')

try:
    numero_int = int(numero)
    par_impar = numero_int  % 2 == 0
    par_impar_texto = 'PAR'
    if par_impar is False:
        par_impar_texto = 'IMPAR'
    print(f'Este numero e {par_impar_texto}.')
except:
    print('Voce nao digitou um numero inteiro.')