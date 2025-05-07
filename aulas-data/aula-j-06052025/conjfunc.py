vl = [3,8,2.5,6,10,9]

def calcula_valor_maximo_lista(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

def calcula_valor_minimo_lista(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def calcula_soma_lista(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma

def quantidade_itens_lista(lista):
    i = 0
    for item in lista:
        i = i + 1
    return i

def totalminmax(lista):
    total = calcula_soma_lista(lista)
    min = calcula_valor_minimo_lista(lista)
    max = calcula_valor_maximo_lista(lista)
    return total, min, max

print(calcula_valor_maximo_lista(vl))
print(calcula_valor_minimo_lista(vl))
print(calcula_soma_lista(vl))
print(quantidade_itens_lista(vl))