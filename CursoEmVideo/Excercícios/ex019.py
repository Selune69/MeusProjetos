import random
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('DIgite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print(f'o aluno escolhido foi {escolhido}!')
