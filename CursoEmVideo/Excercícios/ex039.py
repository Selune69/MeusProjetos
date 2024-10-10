from datetime import date
nasc = int(input('Ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - nasc

print(f'Quem nasceu em {nasc} tem {idade} em {anoatual}')

if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para você se alistar.')
    ano = saldo + anoatual
    print(f'Seu alistamento será em {ano}')
elif idade == 18:
    print('Você precisa de alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há mais de {saldo} anos.')
    ano = anoatual - saldo
    print(f'Você deveria ter se alistado no ano de {ano}')
