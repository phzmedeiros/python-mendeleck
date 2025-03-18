# IMPORTAÇÃO DA BIBLIOTECA MATH PARA OS CALCULOS
import math

# TÍTULO DO PROGRAMA
print("*********************************************************")
print("*** CÁLCULO DA POSIÇÃO DE UM PROJÉTIL ISRÁPIDOPOLENSE ***")
print("*********************************************************")

# ENTRADA DE DADOS
velocidade_inicial = float(input("\nInsira a velocidade inicial do projétil (m/s): "))
angulo_graus = float(input("\nInsira o ângulo de lançamento do projétil (graus): "))
tempo = float(input("\nInsira o tempo de movimento do projétil em segundos (s): "))

# CONVERSÃO DE UNIDADES
angulo_radiano = (angulo_graus * math.pi) / 180

# CÁLCULO DA POSIÇÃO
posicao_x = velocidade_inicial * math.cos(angulo_radiano) * tempo
posicao_y = (velocidade_inicial * math.sin(angulo_radiano) * tempo) - (5 * (tempo**2))

# SAÍDA DE DADOS
print("\n\n******************")
print("*** RESULTADOS ***")
print("******************")
print(f"\nPosição horizontal (x): {posicao_x:.2f} m")
print(f"\nPosição vertical (y): {posicao_y:.2f} m\n\n")