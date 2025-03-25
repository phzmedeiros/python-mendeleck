while(True):
    try:
        nota1 = float(input("Digite a nota: "))
        print("Nota: ", nota1)
        break
    except:
        print("\nAtenção digitar somente números")
