alunos = {
    "João": [7.5, 8.0, 6.0],
    "Maria": [9.0, 8.5, 10.0],
    "Pedro": [5.0, 6.5, 7.0]
}

def calcular_media(notas):
    return sum(notas) / len(notas)

for aluno, notas in alunos.items():
    media = calcular_media(notas)
    print(aluno, f'{media:.1f}')