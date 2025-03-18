print("********************************")
print("    CALCULADORA KASSYUZ")
print("********************************\n")

print("Operações disponíveis:")
print(" +  -> Adição")
print(" -  -> Subtração")
print(" *  -> Multiplicação")
print(" /  -> Divisão")

# Entrada dos valores na ordem: primeiro valor, operação e segundo valor
valor1 = float(input("\nDigite o primeiro valor: "))
operacao = input("Digite a operação desejada: ")
valor2 = float(input("Digite o segundo valor: "))

# Processamento e exibição do resultado
if operacao == '+':
    resultado = valor1 + valor2
    print(f"\nResultado: {valor1} + {valor2} = {resultado:.2f}")
elif operacao == '-':
    resultado = valor1 - valor2
    print(f"\nResultado: {valor1} - {valor2} = {resultado:.2f}")
elif operacao == '*':
    resultado = valor1 * valor2
    print(f"\nResultado: {valor1} * {valor2} = {resultado:.2f}")
elif operacao == '/':
    if valor2 == 0:
        print("\nErro: Divisão por zero não é permitida!")
    else:
        resultado = valor1 / valor2
        print(f"\nResultado: {valor1} / {valor2} = {resultado:.2f}")
else:
    print("\nOperação inválida!")