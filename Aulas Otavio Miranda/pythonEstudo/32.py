pessoa = {'nome': 'Aline',
          'sobrenome': 'Souza',
          }

(a1, a2), (b1, b2) = pessoa.items()

print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)