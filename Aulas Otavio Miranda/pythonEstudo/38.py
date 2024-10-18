lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

print(dict(lista))
print()
print(dc)