# -------------------------------
#  Exercício 1
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [1, 0, 1]
C = [0, 0, 0]
for i in range(3):
    soma = 0
    for j in range(3):
        soma += A[i][j] * B[j]
    C[i] = soma
print("Vetor resultante C:")
for i in range(3):
    print(f"C[{i}] = {C[i]}")

# -------------------------------
# Exercício 2
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(3):
    for j in range(3):
        soma = 0
        for k in range(3):
            soma += A[i][k] * B[k][j]
        C[i][j] = soma
print("\nMatriz resultante C:")
for i in range(3):
    print(C[i])

# -------------------------------
# Exercício 3
tabela = [
    ["Produto", "Farinha [g]", "Açúcar [g]", "Frutas [g]", "Leite [L]", "Aveia [g]",
     "Fermento [g]", "Creme [g]", "Nozes [g]", "Chocolate [g]", "Avelã [g]", "Manteiga [g]", "Ovos [unidade]"],
    ["Macarons", 25, 3, 5, 0.03, 2, 2, 5, 0, 5, 1, 5, 0.2],
    ["Profiteroles", 30, 2, 1, 0.035, 0, 1, 2, 0, 2, 2, 5, 0.4],
    ["Mille Feuille", 20, 4, 2, 0.05, 0, 1, 5, 1, 5, 5, 5, 0.5],
    ["Canelé", 40, 2, 2, 0.035, 5, 1, 5, 1, 5, 5, 10, 0.5],
    ["Petit Gâteau", 35, 3, 1, 0.04, 2, 1, 10, 3, 10, 3, 5, 0.5],
    ["Crème Brûlée", 20, 2, 1, 0.05, 1, 1, 5, 0, 5, 0, 5, 0.5],
    ["Crêpe Suzette", 25, 3, 2, 0.045, 2, 1, 5, 1, 5, 1, 5, 0.4],
    ["Madeleine", 30, 3, 2, 0.05, 2, 1, 5, 2, 5, 2, 10, 0.5],
    ["Saint Honoré", 40, 5, 3, 0.06, 10, 3, 15, 5, 15, 5, 10, 0.5],
    ["Gâteau Opéra", 50, 7, 4, 0.07, 15, 4, 20, 10, 20, 10, 10, 0.6],
    ["Crème au Citron", 50, 7, 4, 0.055, 10, 3, 15, 5, 15, 5, 10, 0.6]
]
print("\nTabela de ingredientes por produto:\n")
for i in range(len(tabela)):
    for j in range(len(tabela[i])):
        print(f"{tabela[i][j]:<18}", end=" ")
    print()

# -------------------------------
# Exercício 4
ingredientes = [
    [25, 3, 5, 0.03, 2, 2, 5, 0, 5, 1, 5, 0.2],
    [30, 2, 1, 0.035, 0, 1, 2, 0, 2, 2, 5, 0.4],
    [20, 4, 2, 0.05, 0, 1, 5, 1, 5, 5, 5, 0.5],
    [40, 2, 2, 0.035, 5, 1, 5, 1, 5, 5, 10, 0.5],
    [35, 3, 1, 0.04, 2, 1, 10, 3, 10, 3, 5, 0.5],
    [20, 2, 1, 0.05, 1, 1, 5, 0, 5, 0, 5, 0.5],
    [25, 3, 2, 0.045, 2, 1, 5, 1, 5, 1, 5, 0.4],
    [30, 3, 2, 0.05, 2, 1, 5, 2, 5, 2, 10, 0.5],
    [40, 5, 3, 0.06, 10, 3, 15, 5, 15, 5, 10, 0.5],
    [50, 7, 4, 0.07, 15, 4, 20, 10, 20, 10, 10, 0.6],
    [50, 7, 4, 0.055, 10, 3, 15, 5, 15, 5, 10, 0.6]
]
produtos = [
    "Macarons",
    "Profiteroles",
    "Mille Feuille",
    "Canelé",
    "Petit Gâteau",
    "Crème Brûlée",
    "Crêpe Suzette",
    "Madeleine",
    "Saint Honoré",
    "Gâteau Opéra",
    "Crème au Citron"
]
nomes_ingredientes = ["Farinha [g]", "Açúcar [g]", "Frutas [g]", "Leite [L]", "Aveia [g]",
                      "Fermento [g]", "Creme [g]", "Nozes [g]", "Chocolate [g]", "Avelã [g]",
                      "Manteiga [g]", "Ovos [unidade]"]
quantidade_produtos = []

print("\nDigite a quantidade a ser produzida de cada produto:\n")

for i in range(len(produtos)):
    qtd = int(input(f"{produtos[i]}: "))
    quantidade_produtos.append(qtd)
ingredientes_totais = [0] * len(nomes_ingredientes)

for i in range(len(produtos)):
    for j in range(len(nomes_ingredientes)):
        ingredientes_totais[j] += ingredientes[i][j] * quantidade_produtos[i]
print("\nQuantidade total de ingredientes necessária:\n")
for i in range(len(nomes_ingredientes)):
    print(f"{nomes_ingredientes[i]}: {ingredientes_totais[i]:.2f}")
