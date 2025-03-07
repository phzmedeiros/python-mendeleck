# TITULO DO PROGRAMA
print("**********************")
print("*** DIVISIBILIDADE ***")
print("**********************\n")

# ENTRADA DE DADOS
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# CONDICIONAL PARA VERIFICAÇÃO DE DIVISIBILIDADE E RESPOSTA DO PROGRAMA
if num2 == 0:
    print("Divisão por zero não é permitida.")
elif num1 % num2 == 0:
    print(f"{num1} é divisível por {num2}.")
else:
    print(f"{num1} não é divisível por {num2}.")