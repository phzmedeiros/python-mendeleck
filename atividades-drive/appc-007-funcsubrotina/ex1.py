numero = input("DIGITE O NUMERO: ")

def separarnumero(numero):
    numstr = str(numero)
    digitos = []
    for digito in numstr:
        digitos.append(int(digito))
    return digitos

resultado = separarnumero(numero)
print(resultado)