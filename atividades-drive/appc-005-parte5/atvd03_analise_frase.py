print("**************************************")
print("** ANÁLISE DE FRASE - TTAATTUU **")
print("**************************************")

frase = input("\nDigite uma frase: ")

vogais = "aeiouAEIOU"
especiais = ",.#$%?!"
espacos = vog = cons = esp = 0
contagem_vogais = [0,0,0,0,0]  # a, e, i, o, u

for letra in frase:
    if letra == " ":
        espacos += 1
    elif letra in vogais:
        vog += 1
        if letra.lower() == 'a':
            contagem_vogais[0] +=1
        elif letra.lower() == 'e':
            contagem_vogais[1] +=1
        elif letra.lower() == 'i':
            contagem_vogais[2] +=1
        elif letra.lower() == 'o':
            contagem_vogais[3] +=1
        elif letra.lower() == 'u':
            contagem_vogais[4] +=1
    elif letra.isalpha():
        cons += 1
    elif letra in especiais:
        esp += 1

# Resultados
print(f"\nEspaços: {espacos}")
print(f"Vogais: {vog}")
print(f"Consoantes: {cons}")
print(f"Caracteres especiais: {esp}")

print("\nContagem de cada vogal:")
print(f"A: {contagem_vogais[0]}")
print(f"E: {contagem_vogais[1]}")
print(f"I: {contagem_vogais[2]}")
print(f"O: {contagem_vogais[3]}")
print(f"U: {contagem_vogais[4]}")

letra = input("\nDigite uma letra para contar ocorrências: ")
ocorrencias = frase.count(letra)
print(f"A letra '{letra}' apareceu {ocorrencias} vez(es).")
