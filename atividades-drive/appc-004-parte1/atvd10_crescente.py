# Título de entrada
print("************************************")
print("**TESTE DE ORDENAÇÃO POR CRESCENTE**")
print("************************************")

# Leitura dos 3 números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Verificando se estão em ordem crescente
if n1 < n2 and n2 < n3:
    resultado = "Os números estão em ordem crescente."
else:
    resultado = "Os números não estão em ordem crescente."

# Título de saída
print("*************")
print("**RESULTADO**")
print("*************")
print(resultado)