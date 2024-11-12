try:
    a = 18
    b = 0

    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero.')
except NameError as error:
    print('Nome b não está definido')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')