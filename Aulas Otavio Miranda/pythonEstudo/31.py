def executa(Funcao, *Args):
    return Funcao(*Args)

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    10
)
print(duplica(2))