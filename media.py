""" A média aritmética é dada por 𝑥̅=
∑ 𝑥𝑖
𝑛
𝑖=1
𝑛
. Use a fórmula para obter a média da altura de 5 indivíduos
que medem 1,80; 1,65; 1,72; 1,82; 1,91 metros. Desenvolva um programa em python que pergunte o
tamanho da sequência e realize a média desejada pedindo valor por valor """

print("Exercicios de matemática discreta aplicado ao pyhton- média")
listaAlturas = []
for i in range(5):
    altura = float(input("Selecione uma altura: "))
    listaAlturas.append(altura)

print("Alturas = ", listaAlturas)

soma = sum(listaAlturas)
media = soma/5
print("A média das alturas inseridas é", media)


