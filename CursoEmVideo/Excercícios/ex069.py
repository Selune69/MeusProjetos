print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)

idade = 0
maiorI = totHomem = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)
    
    if idade >= 18:
        maiorI = maiorI + 1
    if sexo == 'M':
        totHomem = totHomem + 1
    if sexo == 'F' and idade < 20:
        mulheres = mulheres + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?')).strip().upper()[0]
    if resp == 'N':
        break

print(f'''Total de pessoas com mais de 18 anos: {maiorI}
Ao todo temos {totHomem} homens cadastrados
E {mulheres} mulheres com menos de 20 anos.''')