média = 0
somaidade = 0
maiorhomem = 0
nomehomem = ''
totmulher = 0
for c in range (1, 5):
    print(f'---- {c}º PESSOA ----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        totmulher = totmulher + 1
média = somaidade / 4
print(f'A média de idade do grupo é de {média}.')
print(f'O home mais velho tem {maiorhomem} anos e se chama {nomehomem}.')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos.')
