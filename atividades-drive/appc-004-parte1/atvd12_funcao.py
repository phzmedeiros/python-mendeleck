# Título de entrada
print("***************************")
print("** CALCULO RAPIDOPOLENSE **")
print("***************************")

# Leitura do valor de x
x = float(input("Digite o valor de x: "))

# Verificando se x é zero para evitar divisão por zero
if x == 0:
    resultado = "Divisão por zero! Não é possivel calcular f(x)."
else:
    resultado = (4 * x**2 - 3 * x + 9) / x

# Título de saída
print("*****************************")
print("** RESULTADO RAPIDOPOLENSE **")
print("*****************************")
print(f"f({x}) = {resultado:.2f}")
