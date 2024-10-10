frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for c in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[c]

print(junto ,inverso )

if junto == inverso:
    print('Temos um palindromo.')
else:
    print('Não temos um palindromo.')
