lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')
for verbo in lista:
    print(f'\nNa palavra {verbo} temos: ', end='')
    for letra in verbo:
        if letra.lower() in 'aeiou':
            print(letra, end='')
