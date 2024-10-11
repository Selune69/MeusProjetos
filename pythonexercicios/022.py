estoque = {
    "maca": 10,
    "banana": 20,
    "laranja": 15
}

def adicionar_item(item, quantidade):
    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade

def remover_item(item, quantidade):
    if item in estoque:
        estoque[item] -= quantidade
        if estoque[item] <= 0:
            del estoque[item]
    else:
        print('Item nao encontrado no estoque!')

def consultar_item(item):
    return estoque.get(item, 'Item nao encontrado no estoque!')

adicionar_item("maca", 5)
remover_item('banana', 25)
print(consultar_item('maca'))
print(estoque)