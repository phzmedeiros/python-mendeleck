i = 0
media = 0
notas = []
while i < 2:
    try:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        i = i + 1
    except:
        print("\nAtenção digitar somente números")

media = (notas[0] + notas[1]) / 2
print("\nMédia: ", media)

i = 0
while i < 2:
    print(f"Nota {i+1}: ", notas[i])
    i = i + 1
