seq = input("digite a sequencia de caracteres numericos = ")
soma = 0
for i in seq:
    soma = soma + int(i)
    print("numeros",i)
print("soma de tudo",soma)

############################################################

soma = 0
tam = len(pl)
for pos in range(0,tam):
    print(pos,"\t",pl[pos])
    soma=soma+int(pl[pos])
print("soma de tudo",soma)

############################################################