print("*******************************************************")
print("** VERIFICAÇÃO DE CÓDIGO DE TORCEDOR DO RaFA FC 🌟 **")
print("*******************************************************")

codigo = input("\nDigite o código do torcedor (7 dígitos): ")

if len(codigo) == 7:
    soma = int(codigo[0]) + int(codigo[1]) + int(codigo[2]) + int(codigo[3]) + int(codigo[4]) + int(codigo[5])
    verificador_calculado = soma % 10

    print("\n--------------------------------------------")
    print("Cálculo do Dígito Verificador")
    print("--------------------------------------------")
    print("Soma dos 6 primeiros dígitos:", soma)
    print("Dígito verificador calculado:", verificador_calculado)
    print("Dígito verificador informado :", codigo[6])

    if verificador_calculado == int(codigo[6]):
        print("\nCÓDIGO VÁLIDO! O torcedor é verdadeiro!")
    else:
        print("\nCÓDIGO INVÁLIDO!")
else:
    print("\nCódigo inválido: deve conter exatamente 7 dígitos numéricos.")