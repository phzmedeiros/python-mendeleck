print("*****************************************")
print("**** SISTEMA DE AVALIAÇÃO DE PRESSÃO ****")
print("*****************************************\n")

nome = input("Digite o nome do paciente: ")

while True:
    try:
        pressao1 = float(input("Digite o 1º valor da pressão arterial: "))
        break
    except ValueError:
        print("Atenção, digite somente números!")

while True:
    try:
        pressao2 = float(input("Digite o 2º valor da pressão arterial: "))
        break
    except ValueError:
        print("Atenção, digite somente números!")

while True:
    try:
        pressao3 = float(input("Digite o 3º valor da pressão arterial: "))
        break
    except ValueError:
        print("Atenção, digite somente números!")

media_pressao = (pressao1 + pressao2 + pressao3) / 3

print("\n*************** RESULTADO ***************")
print(f"Paciente: {nome}")
print(f"Média da pressão arterial: {media_pressao:.2f}")

if media_pressao > 12:
    print("Procure um médico")
else:
    print("Sua pressão está ok")