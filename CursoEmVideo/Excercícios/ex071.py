print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)

n = int(input('Que valor voce quer sacar? R$'))

total = n
cel = 100
totcel = 0

while True:
    if total >= cel:
        total = total - cel
        totcel = totcel + 1
    else:
        if totcel > 0:
            print(f'Total de {totcel} cedula de R${cel}')
        if cel == 100:
            cel = 50
        elif cel == 50:
            cel = 20
        elif cel == 20:
            cel = 10
        elif cel == 10:
            cel = 1
        totcel = 0
        if total == 0:
            break