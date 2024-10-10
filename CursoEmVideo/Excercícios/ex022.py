nome = str(input('Qual o seu nome? ')).strip()

print('Analisando seu nome ........')

nome1 = len(nome) - nome.count(' ')
nome2 = len(nome.split()[0])

print(f'Maiusculo: {nome.upper()}')
print(f'Minusculo: {nome.lower()}')
print(f'Seu nome tem letras ao todo: {nome1}')
print(f'Seu primeiro nome tem letras ao todo: {nome2}')
