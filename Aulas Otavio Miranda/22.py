def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplo = criar_multiplicador(2)
triplo = criar_multiplicador(3)
quadruplo = criar_multiplicador(4)

print(duplo(5))
print(triplo(5))
print(quadruplo(5))