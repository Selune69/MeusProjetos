r = str(input('Informe seu sexo:')).upper().strip()[0]
while r not in 'MF':
    r = str(input('Dado inválido. Por favor informe o seu sexo:')).strip().upper()[0]
print(f'Sexo {r} registrado com sucesso.')
