string = 'Milene'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())

else:
    print('Metodo nao existe.')