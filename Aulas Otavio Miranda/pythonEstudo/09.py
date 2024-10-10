from os import system

lista = []
while True:
    print('Selecione Opcao.')
    escolha = str(input('[i]nserir [a]pagar [l]istar: '))

    if escolha in 'Ii':
        system("cls")
        valor = input('Valor: ')
        lista.append(valor)

    elif escolha in 'Aa':
        indice_str = input('Escolha o indice para apagar. ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Nao foi possivel apagar esse indice. ')

    elif escolha in 'Ll':
        system("cls")
        if len(lista) == 0:
            print('Nada para listar.')
        for i, valor in enumerate(lista):
                print(i, valor)

