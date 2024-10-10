time = ('Corinthins', 'Palmeiras', 'Santos',
        'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'Sao Paulo',
        'Fluminense', 'Sport Recife', 'EC Vitoria', 'Coritiba',
        'Avai', 'Ponte Preta', 'Atletic-GO')

print('-=' * 40)
print(f'Lista de times: {time}')
print('-=' * 40)
print(f'Os 5 primeiros times sao : {time[0:5]}')
print('-=' * 40)
print(f'Os ultimos 4 colocados sao: {time[-4:]}')
print('-=' * 40)
print(f'Times em ordem alfabetica: {sorted(time)}')
print('-=' * 40)
print(f'O time da chapecoense esta na posicao {time.index("Chapecoense")+1} posicao.')