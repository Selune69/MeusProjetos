total_verdadeiras = total_negativas = 0
pessoa = ''
lista_perguntas = [str(input('Telefonou para a vitima? ')), str(input('Esteve no local do crime? ')),
         str(input('Mora perto da vitima? ')), str(input('Devia para a vitima? ')),
         str(input('Ja trabalhou com a vitima? '))]
for pergunta in lista_perguntas:
    if pergunta in 'Ss':
        total_verdadeiras += 1
    elif pergunta in 'Nn':
        total_negativas += 1
if total_verdadeiras == 2:
    pessoa = 'Suspeita'
elif total_verdadeiras == 3 or total_verdadeiras == 4:
    pessoa = 'Cumplice'
elif total_verdadeiras == 5:
    pessoa = 'Assasina'
else:
    pessoa = 'Inocente'
print(f'''A pessoa entrevistada respondeu positivo para 
{total_verdadeiras} perguntas e negativo para {total_negativas}
perguntas. Portanto ela e considerada {pessoa}''')