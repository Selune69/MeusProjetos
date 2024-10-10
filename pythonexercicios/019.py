frase = input('Digite uma frase: ')
contagem_palavras = {}

palavras = frase.split()

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)