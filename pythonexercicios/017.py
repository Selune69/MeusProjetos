def soma_numeros():
    total = 0
    while True:
        try:
            numero = int(input('Digite um número (ou 0 para sair): '))
            if numero == 0:
                break
            total += numero
        except ValueError:
            print("Por favor, digite um número válido.")
    print(f"O total é {total}.")