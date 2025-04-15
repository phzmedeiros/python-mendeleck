while(True):
    try:
        nota1 = float(input("Digite a nota 1: "))
        break
    except ValueError:
        print("\nAtenção digitar somente números")

while(True):
    try:
        nota2 = float(input("Digite a nota 2: "))
        break
    except ValueError:
        print("\nAtenção digitar somente números")

while(True):
    try:
        nota3 = float(input("Digite a nota 3: "))
        break
    except ValueError:
        print("\nAtenção digitar somente números")

while(True):
    try:
        nota4 = float(input("Digite a nota 4: "))
        break
    except ValueError:
        print("\nAtenção digitar somente números")

media = (nota1 + nota2 + nota3 + nota4) / 4
print("\nMédia: ", media)