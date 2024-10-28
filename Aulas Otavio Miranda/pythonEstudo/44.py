from sys import getsizeof

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(getsizeof(lista))
print(getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))