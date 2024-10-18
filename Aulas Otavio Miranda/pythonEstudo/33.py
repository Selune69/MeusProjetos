pessoa = {'nome': 'Aline',
          'sobrenome': 'Souza',
          }

dados_pessoa = {'idade': 16,
                'altura': 1.6,
                }

pessoa_completa = {**pessoa, **dados_pessoa, 'chave': 1}

print(pessoa_completa)

def mostro_arg_nomeados(*args, **kwargs):
    print('Nao Nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_arg_nomeados(1, 2, nome='Joana', qlq=123)
