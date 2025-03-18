print("***********")
print("**TABUADA**")
print("***********")

# LEITURA DO NÚMERO
n = int(input("Digite um número para ver sua tabuada: "))

# IMPRESSÃO DA TABUADA
print(f"\nTabuada de {n}:")
i = 0
while i < 10:
    print(f"{n} x {i} = {n * i}")
    i = i + 1