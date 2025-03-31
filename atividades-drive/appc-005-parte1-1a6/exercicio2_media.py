print("***********************")
print("**CÁLCULO VALOR MÉDIo**")
print("***********************")

# LEITURA DO NÚMERO DE VALORES
n = int(input("Quantos valores você irá digitar? "))
soma = 0.0

# LEITURA DOS VALORES E CÁLCULO DA SOMA
i = 1
while i <= n:
    valor = float(input(f"Digite o {i}º valor: "))
    soma = soma + valor
    i = i + 1

# CÁLCULO E IMPRESSÃO DA MÉDIA
media = soma / n
print(f"\nValor médio: {media:.2f}")