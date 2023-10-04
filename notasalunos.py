""" Faça um Programa que peça as quatro notas de 6 alunos, calcule e armazene num
vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a
7.0. """

notas = [[0 for _ in range(4)] for _ in range(6)]
soma = 0

for i in range(6):
    for j in range(4):
        notas[i][j] = float(input(f"Digite a {j+1}ª nota do aluno {i+1}: "))

print(f"As notas dos alunos são {notas}")
medias_alunos = []

# Calcule a média das notas de cada aluno e armazene na lista de médias
for i in range(6):
    soma = sum(notas[i])
    media = soma / len(notas[i])
    medias_alunos.append(media)

# Imprima as médias dos alunos
for i, media in enumerate(medias_alunos):
    print(f"A média do aluno {i+1} é: {media}")
# Conte o número de alunos com média maior ou igual a 7.0
alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)

# Imprima o número de alunos aprovados
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")