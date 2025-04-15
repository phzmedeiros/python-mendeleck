dados = [
    ["João", 25, "M"],
    ["Maria", 30, "F"],
    ["José", 22, "M"],
    ["Ana", 28, "F"],
    ["Pedro", 35, "M"],
    ["Lucas", 20, "M"],
    ["Mariana", 27, "F"],
    ["Carlos", 32, "M"],
    ["Fernanda", 29, "F"],
    ["Ricardo", 31, "M"],
    ["Patrícia", 26, "F"],
    ["Gabriel", 24, "M"],
    ["Juliana", 33, "F"],
    ["Thiago", 21, "M"],
    ["Larissa", 34, "F"],
    ["Eduardo", 23, "M"],
    ["Camila", 36, "F"],
    ["André", 19, "M"],
    ["Roberta", 38, "F"],
    ["Felipe", 37, "M"],
    ["Tatiane", 39, "F"],
    ["Bruno", 40, "M"],
    ["Aline", 41, "F"],
    ["Rafael", 42, "M"],
    ["Vanessa", 43, "F"],
    ["Gustavo", 44, "M"],
    ["Sabrina", 45, "F"],
    ["Diego", 46, "M"],
    ["Claudia", 47, "F"],
    ["Leonardo", 48, "M"],
    ["Juliana", 49, "F"]
]

tam = len(dados)

# print("versao1")
# for pos in range(0, tam):
#     print(pos, "\t", dados[pos])

# print("versao2")
# for registro in dados:
#     print(registro)

# print('versao3')
# for registro in dados:
#     print("nome", registro[0])
#     print("idade", registro[1])
#     print("sexo", registro[2])
#     print("\n")



numero_homens = 0
numero_mulheres = 0
soma = 0
mais_velho = dados[0]
menos_velho = dados[0]

for pessoa in dados:
    soma = soma + pessoa[1]
    if pessoa[2] == "M":
        numero_homens = numero_homens + 1
    else:
        numero_mulheres = numero_mulheres + 1
    if pessoa[1] > mais_velho[1]:
        mais_velho = pessoa
    if pessoa[1] < menos_velho[1]:
        menos_velho = pessoa

media = soma / tam

print(f"Homens: {numero_homens}, Mulheres: {numero_mulheres}")
print(f"Média de idade: {media:}")
print(f"Mais velho: {mais_velho[0]} ({mais_velho[1]} anos)")
print(f"Mais novo: {menos_velho[0]} ({menos_velho[1]} anos)")