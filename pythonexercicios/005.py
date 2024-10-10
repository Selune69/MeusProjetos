from datetime import date, timedelta
data_atual = date.today()
data_futura = data_atual + timedelta(2)
print(f'Hoje e {data_atual}')
print(f'Em dois dias sera {data_futura}')