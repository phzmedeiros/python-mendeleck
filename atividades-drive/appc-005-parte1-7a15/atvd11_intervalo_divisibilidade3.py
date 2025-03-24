print("**************************")
print("** DIVISIBILIDADE POR 3 **")
print("**************************")

inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

print(f"Números divisíveis por 3 no intervalo de {inicio} a {fim}:")
numero = inicio
while numero <= fim:
    if numero % 3 == 0:
        print(numero)
    numero = numero + 1