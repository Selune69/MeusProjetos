try:
    print('ABRIR ARQUIVO')
    8/0

except ZeroDivisionError:
    print('Dividiu o zero')

else:
    print('Nao deu erro')

finally:
    print('FECHAR ARQUIVO')