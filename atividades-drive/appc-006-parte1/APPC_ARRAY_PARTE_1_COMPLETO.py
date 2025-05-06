# -------------------------------
# Exercício 1
valores = []
n = -1
while n <= 0:
    try:
        n = int(input("Digite a quantidade de valores que deseja inserir: "))
        if n <= 0:
            print("Por favor, digite um número inteiro positivo.")
    except:
        print("Entrada inválida. Tente novamente.")

for i in range(n):
    valor = int(input(f"Digite o valor [{i}]: "))
    valores.append(valor)

maior = valores[0]
menor = valores[0]
soma = 0

for i in range(n):
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]
    soma += valores[i]

media = soma / n

print("\n***********************")
print("VALORES DIGITADOS: ")
for i in range(n):
    print(f"VALOR [{i}] = {valores[i]}")
print("\nMAIOR VALOR =", maior)
print("MENOR VALOR =", menor)
print("MÉDIA ARITMÉTICA = {:.2f}".format(media))
print("***********************")

# -------------------------------
# Exercício 2
valores = []
n = int(input("Digite a quantidade de valores: "))
for i in range(n):
    valor = int(input(f"Digite o valor [{i}]: "))
    valores.append(valor)
print("\nVALORES EM ORDEM INVERSA:")
i = n - 1
while i >= 0:
    print(f"VALOR [{i}] = {valores[i]}")
    i = i - 1

# -------------------------------
# Exercício 3
n = int(input("Digite a quantidade de alunos: "))
notas = []
medias = []
for i in range(n):
    print(f"\nDigite os dados do aluno [{i}]:")
    ra = input("Digite o RA do aluno: ")
    linha = [ra]
    soma = 0
    for j in range(4):
        nota = -1
        while nota < 0 or nota > 10:
            try:
                nota = float(input(f"Nota {j + 1}: "))
                if nota < 0 or nota > 10:
                    print("Nota deve estar entre 0 e 10.")
            except:
                print("Entrada inválida. Digite um número.")
        linha.append(nota)
        soma += nota
    notas.append(linha)
    medias.append(soma / 4)
print("\n********** NOTAS E MÉDIAS **********")
for i in range(n):
    print(f"RA: {notas[i][0]}  Notas: {notas[i][1:]}  Média: {medias[i]:.2f}")

# -------------------------------
# Exercício 4
valores = []
n = int(input("Digite a quantidade de valores: "))
for i in range(n):
    valor = int(input(f"Digite o valor [{i}]: "))
    valores.append(valor)
valores.sort()
print("\nVALORES EM ORDEM CRESCENTE:")
for i in range(n):
    print(f"VALOR [{i}] = {valores[i]}")

# -------------------------------
# Exercício 5
valores = []
n = int(input("Digite a quantidade de valores: "))
for i in range(n):
    valor = int(input(f"Digite o valor [{i}]: "))
    valores.append(valor)
for i in range(n):
    for j in range(i + 1, n):
        if valores[i] > valores[j]:
            temp = valores[i]
            valores[i] = valores[j]
            valores[j] = temp
print("\nVALORES EM ORDEM CRESCENTE:")
for i in range(n):
    print(f"VALOR [{i}] = {valores[i]}")

# -------------------------------
# Exercício 6
num = int(input("Digite um número inteiro: "))
binario = []
if num == 0:
    binario.append(0)
else:
    while num > 0:
        resto = num % 2
        binario.insert(0, resto)
        num = num // 2
print("\nBINÁRIO:", end=" ")
for i in range(len(binario)):
    print(binario[i], end="")
print("\nVETOR:", binario)

# -------------------------------
# Exercício 7
import math
n = int(input("Digite a quantidade de pontos da fazenda: "))
pontos = []
for i in range(n):
    print(f"\nDigite as coordenadas do ponto [{i}]:")
    x = float(input("X: "))
    y = float(input("Y: "))
    pontos.append([x, y])
perimetro = 0
for i in range(n):
    x1 = pontos[i][0]
    y1 = pontos[i][1]
    if i == n - 1:
        x2 = pontos[0][0]
        y2 = pontos[0][1]
    else:
        x2 = pontos[i + 1][0]
        y2 = pontos[i + 1][1]
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    perimetro += distancia
print("\nO perímetro da fazenda é: {:.2f}".format(perimetro))

# -------------------------------
# Exercício 8
nomes = []
n = int(input("Digite a quantidade de nomes: "))
for i in range(n):
    nome = input(f"Digite o nome [{i}]: ")
    nomes.append(nome)
consulta = input("\nDigite o nome que deseja consultar: ")
if consulta in nomes:
    print("Nome CADASTRADO!")
else:
    print("Nome NÃO cadastrado.")

# -------------------------------
# Exercício 9
n = int(input("Digite o número de linhas da pirâmide: "))
for i in range(1, n + 1):
    print("*" * i)

# -------------------------------
# Exercício 10
n = int(input("Digite o número de linhas da pirâmide: "))
for i in range(1, n + 1):
    espacos = n - i
    estrelas = 2 * i - 1
    print(" " * espacos + "*" * estrelas)

# -------------------------------
# Exercício 11
n = int(input("Digite a quantidade de alunos: "))
alunos = []
for i in range(n):
    print(f"\nDigite os dados do aluno [{i}]:")
    ra = input("RA do aluno: ")
    notas = []
    soma = 0
    for j in range(4):
        nota = -1
        while nota < 0 or nota > 10:
            try:
                nota = float(input(f"Nota {j + 1}: "))
                if nota < 0 or nota > 10:
                    print("Nota deve estar entre 0 e 10.")
            except:
                print("Entrada inválida. Digite um número.")
        notas.append(nota)
        soma += nota
    media = soma / 4
    linha = [ra, notas[0], notas[1], notas[2], notas[3], media]
    alunos.append(linha)
print("\n*********** RELATÓRIO FINAL ***********")
for i in range(n):
    print(f"Aluno {i}: RA = {alunos[i][0]}")
    print(f"Notas: {alunos[i][1]}, {alunos[i][2]}, {alunos[i][3]}, {alunos[i][4]}")
    print(f"Média: {alunos[i][5]:.2f}")
    print("----------------------------------------")