# TITULO DO PROGRAMA
print("****************************************")
print("******* CONVERSOR DE TEMPERATURA *******")
print("****************************************\n")

# EXIBE AS UNIDADES DISPONÍVEIS
print("Unidades disponíveis:")
print(" 1 - Celsius")
print(" 2 - Fahrenheit")
print(" 3 - Kelvin")
print(" 4 - Rankine")
print(" 5 - Réaumur")
print(" 6 - Rømer")
print(" 7 - Newton")
print(" 8 - Delisle\n")

# ENTRADA DE DADOS VALOR E UNIDADE DE ORIGEM
origem = int(input("Selecione a unidade de medida de origem (número): "))
valor_origem = float(input("Digite o valor da temperatura na unidade de medida selecionada: "))
destino = int(input("\nEscolha a unidade de medida de destino (número): "))

# CONVERSÃO DE ORIGEM PARA CELSIUS
if origem == 1:
    celsius = valor_origem
elif origem == 2:
    celsius = (valor_origem - 32) * 5/9
elif origem == 3:
    celsius = valor_origem - 273.15
elif origem == 4:
    celsius = (valor_origem * 5/9) - 273.15
elif origem == 5:
    celsius = valor_origem * 5/4
elif origem == 6:
    celsius = (valor_origem - 7.5) / 0.525
elif origem == 7:
    celsius = valor_origem / 0.33
elif origem == 8:
    celsius = 100 - (valor_origem * 2/3)
else:
    print("Unidade de origem inválida!")
    exit()

# CONVERSÃO DE CELSIUS PARA DESTINO
if destino == 1:
    resultado = celsius
    unidade_destino = "Celsius"
elif destino == 2:
    resultado = celsius * 9/5 + 32
    unidade_destino = "Fahrenheit"
elif destino == 3:
    resultado = celsius + 273.15
    unidade_destino = "Kelvin"
elif destino == 4:
    resultado = (celsius + 273.15) * 9/5
    unidade_destino = "Rankine"
elif destino == 5:
    resultado = celsius * 4/5
    unidade_destino = "Réaumur"
elif destino == 6:
    resultado = celsius * 0.525 + 7.5
    unidade_destino = "Rømer"
elif destino == 7:
    resultado = celsius * 0.33
    unidade_destino = "Newton"
elif destino == 8:
    resultado = (100 - celsius) * 3/2
    unidade_destino = "Delisle"
else:
    print("Unidade de destino inválida!")
    exit()

# Exibição do resultado final
print("\n\n***************************")
print("*** CONVERSÃO REALIZADA ***")
print("***************************\n")
print(f"{valor_origem:.2f} na unidade escolhida foi convertido para {resultado:.2f} {unidade_destino}\n")
