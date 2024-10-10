def palindromo(frase):
    frase = frase.lower().replace(" ", "")
    return frase == frase[::-1]

print(palindromo('Arara'))
print(palindromo('Nao sei'))

#Função para verificar palíndromo