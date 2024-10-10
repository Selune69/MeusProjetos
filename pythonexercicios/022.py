estoque = {
    "maca": 10,
    "banana": 20,
    "laranja": 15
}

def adicionar_item(item, quantidade):
    if item in estoque:
        estoque[item] += quantidade