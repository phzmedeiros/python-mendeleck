# TITULO DO PROGRAMA
print("********************************")
print("*** CONVERSOR DE TEMPERATURA ***")
print("********************************\n")

# ENTRADA DE DADOS - TEMPERATURA EM CELSIUS
celsius = float(input("Digite a temperatura em Celsius: "))

# CÁLCULO DAS CONVERSÕES
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15
rankine = (celsius + 273.15) * 9/5
reaumur = celsius * 4/5

# EXIBIÇÃO DOS RESULTADOS
print("\n***************************")
print("*** CONVERSÃO REALIZADA ***")
print("***************************\n")
print(celsius,"graus em Fahrenheit:", fahrenheit)
print(celsius,"graus em Kelvin:", kelvin)
print(celsius,"graus em Rankine:", rankine)
print(celsius,"graus em Reaumur:", reaumur)
