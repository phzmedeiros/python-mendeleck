print("*********************************")
print("** DIVISIBILIDADE POR X NUMERO **")
print("*********************************")

inicio = int(input("\nDigite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))
divisor = int(input("Digite o divisor: "))

print(f"\nNúmeros divisíveis por {divisor} no intervalo de {inicio} a {fim}:")
numero = inicio
while numero <= fim:
    if numero % divisor == 0:
        print(numero)
    numero = numero + 1