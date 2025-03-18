# IMPORTAÇÃO DA BIBLIOTECA MATH PARA OS CALCULOS
import math

# CÁLCULO DE DISTÂNCIA LINEAR
# TITUO DO PROGRAMA
print("*****************************************************")
print("*** CÁLCULO DE DISTÂNCIA LINEAR ENTRE DOIS PONTOS ***")
print("*****************************************************")

# ENTRADA DE DADOS - COORDENADAS
px = float(input("\nDigite a coordenada X do ponto de origem: "))
py = float(input("Digite a coordenada Y do ponto de origem: "))
qx = float(input("\nDigite a coordenada X do ponto de destino: "))
qy = float(input("Digite a coordenada Y do ponto de destino: "))

# CÁLCULO DA DISTÂNCIA
distancia = math.sqrt((qx - px) ** 2 + (qy - py) ** 2)

# SAÍDA DE DADOS
print("\n******************")
print("*** RESULTADOS ***")
print("******************")
print(f"\nA distância linear entre os pontos é: {distancia:.2f}")