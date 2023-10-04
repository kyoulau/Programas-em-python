vetorCaractere = []
quantidadeConsoantes = 0
consoantesRelacao = []

def iscaracterConsoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    return caractere.lower() in consoantes

for i in range(6):
    caractere = input("DIGITE UM CARACTERE: ")
    vetorCaractere.append(caractere)

for caractere in vetorCaractere:
    if iscaracterConsoante(caractere):
        quantidadeConsoantes += 1
        consoantesRelacao.append(caractere)
 
print(f"CARACTERES: {vetorCaractere}")
print(f"RELAÇÃO CONSOANTES: {consoantesRelacao}")
print("Consoantes lidas:")
for caractere in consoantesRelacao:
    print(f"- {caractere}")
print(f"Total de consoantes lidas: {quantidadeConsoantes}")