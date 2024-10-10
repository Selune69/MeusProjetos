while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite o segundo numero: ')
    numero1_float = 0
    numero2_float = 0
    numero_valido = None
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numero_valido = True
    except:
        numero_valido = None
    if numero_valido is None:
        print('Um ou ambos os numeros sao invalidos.')
        continue
    operadores = '+-/*'
    if operadores not in '+-/*':
        print('Operador invalido.')
        continue
    if len(operadores) > 1:
        print('Digite apenas um operador.')
        continue
    if operadores == '+':
        print(numero1_float + numero2_float)
    elif operadores == '-':
        print(numero1_float - numero2_float)
    elif operadores == '/':
        print(numero1_float / numero2_float)
    elif operadores == '*':
        print(numero1_float * numero2_float)
    else:
        print('Nao deveria chegar aqui')
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    if sair is True:
        break
