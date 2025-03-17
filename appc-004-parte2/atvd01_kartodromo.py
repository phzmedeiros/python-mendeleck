# Título de entrada
print("**************************************************")
print("** KARTÓDROMO DE ALTA VELOCIDADE DE RAPIDÓPOLIS **")
print("**************************************************")

# Leitura dos dados de distância e tempo para cada trecho
s1 = 400  # distância do trecho 1 em metros
t1 = float(input("Digite o tempo (em segundos) para o trecho 1 (400m): "))

s2 = 300  # distância do trecho 2 em metros
t2 = float(input("Digite o tempo (em segundos) para o trecho 2 (300m): "))

s3 = 500  # distância do trecho 3 em metros
t3 = float(input("Digite o tempo (em segundos) para o trecho 3 (500m): "))

s4 = 200  # distância do trecho 4 em metros
t4 = float(input("Digite o tempo (em segundos) para o trecho 4 (200m): "))

s5 = 100  # distância do trecho 5 em metros
t5 = float(input("Digite o tempo (em segundos) para o trecho 5 (100m): "))

# Calculando a velocidade média de cada trecho
v1 = s1 / t1
v2 = s2 / t2
v3 = s3 / t3
v4 = s4 / t4
v5 = s5 / t5

# Calculando a aceleração média de cada trecho (definida como v/t²)
a1 = v1 / (t1 ** 2)
a2 = v2 / (t2 ** 2)
a3 = v3 / (t3 ** 2)
a4 = v4 / (t4 ** 2)
a5 = v5 / (t5 ** 2)

# Calculando a velocidade média do percurso
distancia_total = s1 + s2 + s3 + s4 + s5
tempo_total = t1 + t2 + t3 + t4 + t5
velocidade_media_percurso = distancia_total / tempo_total

# Calculando a aceleração média do percurso
aceleracao_media_percurso = (a1 + a2 + a3 + a4 + a5) / 5

# Título de saída
print("\n\n****************************************")
print("** RESULTADOS DA ANALISE RAPIDOPOLENSE**")
print("****************************************")

# Exibindo os resultados para cada trecho
print(f"\nVelocidade média do trecho 1: {v1:.2f} m/s")
print(f"Aceleração média do trecho 1: {a1:.2f} m/s²")

print(f"\nVelocidade média do trecho 2: {v2:.2f} m/s")
print(f"Aceleração média do trecho 2: {a2:.2f} m/s²")

print(f"\nVelocidade média do trecho 3: {v3:.2f} m/s")
print(f"Aceleração média do trecho 3: {a3:.2f} m/s²")

print(f"\nVelocidade média do trecho 4: {v4:.2f} m/s")
print(f"Aceleração média do trecho 4: {a4:.2f} m/s²")

print(f"\nVelocidade média do trecho 5: {v5:.2f} m/s")
print(f"Aceleração média do trecho 5: {a5:.2f} m/s²")

# Exibindo os resultados do percurso completo
print(f"\nVelocidade média do percurso: {velocidade_media_percurso:.2f} m/s")
print(f"Aceleração média do percurso: {aceleracao_media_percurso:.2f} m/s²")

# Comparação de velocidade entre os trechos
print("\n--- Comparação de velocidade entre os trechos ---")
if v2 > v1:
    print("Trecho 2 foi mais rápido que o Trecho 1.")
else:
    print("Trecho 2 não foi mais rápido que o Trecho 1.")

if v3 > v2:
    print("Trecho 3 foi mais rápido que o Trecho 2.")
else:
    print("Trecho 3 não foi mais rápido que o Trecho 2.")

if v4 > v3:
    print("Trecho 4 foi mais rápido que o Trecho 3.")
else:
    print("Trecho 4 não foi mais rápido que o Trecho 3.")

if v5 > v4:
    print("Trecho 5 foi mais rápido que o Trecho 4.")
else:
    print("Trecho 5 não foi mais rápido que o Trecho 4.")
