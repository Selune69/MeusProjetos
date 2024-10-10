frase = 'O Python é uma linguagem de programação' \
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_maisX = 0
letra_apareceu_maisX = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i = i + 1
        continue

    X_letra_apareceu_atual = frase.count(letra_atual)

    if apareceu_maisX < X_letra_apareceu_atual:
        apareceu_maisX = X_letra_apareceu_atual
        letra_apareceu_maisX = letra_atual

    print(letra_atual, X_letra_apareceu_atual)
    i = i + 1

print('A letra que apareceu mais vezes foi'
f'"{letra_apareceu_maisX}" que apareceu'
f'{apareceu_maisX}x'
)