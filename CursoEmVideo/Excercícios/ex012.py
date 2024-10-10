preço = float(input('Qual o preço do produto? R$'))

novo = preço - (preço * 5 / 100)

print(f'Com o desconto de 5%, o preço do produto é de R${novo:.2f}.')
