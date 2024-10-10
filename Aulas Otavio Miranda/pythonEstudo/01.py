nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')
    print(f'Seu nome contem {' ' in nome} espacos')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')
