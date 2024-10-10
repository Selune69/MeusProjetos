def qts_vogais(palavra):
    vogal = 'aeiouAEIOU'
    c = 0
    for letra in palavra:
        if letra in vogal:
            c += 1
    return c

print(qts_vogais('Milene'))