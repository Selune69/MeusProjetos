pessoa = {
    'nome': 'Milene',
    'sobrenome': 'Borges',
    'idade': 24,
    'endereco': [
        {'rua': 'tal', 'numero': 3,
         'rua2': 'tal2', 'numero2': 5}
    ]
}

print(pessoa['endereco'])
print(pessoa.__len__())