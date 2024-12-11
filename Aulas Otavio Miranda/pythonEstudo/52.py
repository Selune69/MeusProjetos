def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

multi = criar_multiplicador(5)

print(multi(5))