# Programa de Cálculo de IMC
print("***********************")
print("** CÁLCULO DE IMC **")
print("***********************")

# Leitura dos dados
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Baixo peso"
elif imc >= 18.5 and imc <= 24.99:
    classificacao = "Normal"
elif imc >= 25 and imc <= 29.99:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibição dos resultados
print("\n*************************")
print("** RESULTADO DO IMC **")
print("*************************")
print(f"IMC calculado: {imc:.2f}")
print(f"Classificação: {classificacao}")
