lista = []
for numero in range(10):
    lista.append(numero)

#ou

lista = [numero * 2
         for numero in range(10)
         ]

print(lista)
print(list(range(10)))

#ou

lista2 = [numero for numero in range(10) if numero > 5]
print(lista2)
