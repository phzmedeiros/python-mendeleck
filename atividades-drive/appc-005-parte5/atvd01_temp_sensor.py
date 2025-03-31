print("**********************************")
print("** SENSOR DE TEMPERATURA - GGEELLOO **")
print("**********************************")

TEMP = [10, 12, 9, 8, 9, 9, 10, 11, 12, 14, 12, 11]

# Cálculos
media = sum(TEMP) / len(TEMP)
maior = max(TEMP)
menor = min(TEMP)

# Resultados
print(f"\nTemperatura média: {media:.2f}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
