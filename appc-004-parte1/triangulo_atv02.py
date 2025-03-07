# TITULO DO PROGRAMA
print("***********************************")
print("*** CLASSIFICADOR DE TRIÂNGULOS ***")
print("***********************************\n")

# ENTRADA DE DADOS
lado1 = float(input("Insira o valor do primeiro lado do triângulo: "))
lado2 = float(input("Insira o valor do segundo lado do triângulo: "))
lado3 = float(input("Insira o valor do terceiro lado do triângulo: "))

# PRIMEIRO TESTE PARA EVITAR PROBLEMAS COM A CLASSIFICAÇÃO
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # CLASSIFICAÇÃO DO TRIÂNGULO
    if lado1 == lado2 == lado3:
        print("\nO triângulo é Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("\nO triângulo é Isósceles.")
    else:
        print("\nO triângulo é Escaleno.")
else:
    print("\nOs valores informados não formam um triângulo.")
