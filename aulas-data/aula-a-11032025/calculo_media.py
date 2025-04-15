i = 0
soma = 0
while i < 5:
    i = i + 1
    nota = float(input(f"Digite a nota {i}:"))
    soma = soma + nota
media = soma / 5
print("A média é ",format(media,"6.2f"))
