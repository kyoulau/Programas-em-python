import random 
num = []
numero_aleatorio = random.randint(1, 100)
def sorteia():
    for i in range (6):
        numero_aleatorio = random.randint(1, 100)
        num.append(numero_aleatorio)
    return numero_aleatorio

def somaPar():
    pares = [numero for numero in num if numero % 2 == 0]
    soma = sum(pares)
    return pares, soma


sorteia()
pares, soma = somaPar()
print("Números sorteados:", num)
print("Pares ordenados:", pares)
print("Soma dos valores pares:", soma)