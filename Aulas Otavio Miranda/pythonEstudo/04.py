entrada = str(input('Digite seu nome: '))
nome = len(entrada)
if nome <= 4:
    print('Seu nome e curto.')
elif nome >= 5 and nome <= 6:
    print('Seu nome e normal.')
else:
    print('Seu nome e muito grande.')