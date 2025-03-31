print("******************************")
print("**TEMPERATURA DE FERMENTAÇÃO**")
print("******************************")

# CÁLCULO DA MENOR TEMPERATURA
d = 0
temperatura = 0.011 * (d ** 3) - 0.3 * (d ** 2) + 0.04 * d
menor_temp = temperatura
dia_menor = d

d = 1
while d <= 30:
    temperatura = 0.011 * (d ** 3) - 0.3 * (d ** 2) + 0.04 * d
    if temperatura < menor_temp:
        menor_temp = temperatura
        dia_menor = d
    d += 1

# IMPRESSÃO DO DIA COM A MENOR TEMPERATURA
print(f"\nO dia com a menor temperatura prevista é o dia {dia_menor} com {menor_temp:.2f}°C")