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

i = 0
while i < 5:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ")
    dados.append([nome, idade, sexo])
    i = i + 1

print(dados)