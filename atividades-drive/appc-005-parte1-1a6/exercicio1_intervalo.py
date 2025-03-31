print("************************")
print("**INTERVALO DE VALORES**")
print("************************")

# LEITURA DOS VALORES
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# GARANTE QUE VALOR1 SEJA O MENOR
if valor1 > valor2:
    valor1, valor2 = valor2, valor1

# IMPRESSÃO DOS VALORES NO INTERVALO
print(f"\nValores inteiros no intervalo de {valor1} a {valor2}:")
i = valor1
while i <= valor2:
    print(i)
    i = i + 1  # substituindo i += 1