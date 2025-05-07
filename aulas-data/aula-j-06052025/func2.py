vl = [3,8,2.5,6,10,9]

def medialista(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    media = soma / len(lista)
    return media

print(medialista(vl))
