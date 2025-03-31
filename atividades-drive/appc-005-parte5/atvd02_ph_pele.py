print("**************************************")
print("** ANÁLISE DE PH DA PELE - Dra. Panturrilha **")
print("**************************************")

PH = [7, 6, 7.5, 7, 6.8, 7.1, 6.9, 6.4, 6.5, 6.7]

# Cálculos
media = sum(PH) / len(PH)
maior = max(PH)
menor = min(PH)

# Contagem dos valores acima e abaixo da média
acima = abaixo = 0
for valor in PH:
    if valor > media:
        acima += 1
    elif valor < media:
        abaixo += 1

# Resultados
print(f"\nValor médio do PH: {media:.2f}")
print(f"Maior PH: {maior}")
print(f"Menor PH: {menor}")
print(f"Valores acima da média: {acima}")
print(f"Valores abaixo da média: {abaixo}")
