def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3
    print('Vou terminar')

gen = generator(n=0)

print(next(gen)) #chama yield 1
print(next(gen)) #chama yield 2
print(next(gen))
