valor = []
pos = 0

while pos < 5:
    va = float(input(f"Digite o número {pos+1}: "))
    valor.append(va)
    pos = pos + 1

soma = 0
pos = 0
while pos < 5:
    soma = soma + valor[pos]
    pos = pos + 1

media = soma / 5
print(valor)
print(f"A média dos números é: {media}")