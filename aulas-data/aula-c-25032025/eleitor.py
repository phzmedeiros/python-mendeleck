while(True):
    try:
        idade = float(input("Digite a idade: "))
        break
    except ValueError:
        print("\nAtenção digitar somente números")

if (idade < 16):
    print("Não eleitor (abaixo de 16 anos)")
elif (idade >=16) and (idade < 18) or (idade >= 65):
    print("Eleitor facultativo (de 16 a 18 anos e maior de 65 anos, inclusive)")
elif (idade >= 18) and (idade < 65):
    print("Eleitor obrigatório (entre a faixa de 18 e menor de 65 anos)")
else:
    print("Idade inválida")
  