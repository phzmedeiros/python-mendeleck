print("******************************")
print("**MÉDIA, MAIOR E MENOR VALOR**")
print("******************************")

n = int(input("Quantos valores você irá digitar? "))
i = 1
soma = 0
maior = 0
menor = 0

if n > 0:
    valor = float(input("Digite o 1º valor: "))
    soma = soma + valor
    maior = valor
    menor = valor
    i = 2
    while i <= n:
        valor = float(input("Digite o " + str(i) + "º valor: "))
        soma = soma + valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        i = i + 1
    media = soma / n
    print("\nValor médio: " + format(media, ".2f"))
    print("Maior valor: " + format(maior, ".2f"))
    print("Menor valor: " + format(menor, ".2f"))
else:
    print("Nenhum valor foi digitado.")