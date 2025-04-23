data = [
    ["Pedro Henrique", 19, 1.73],
    ["Lucas", 20, 1.80],
    ["Mariana", 27, 1.65],
    ["Carlos", 32, 1.75],
    ["Fernanda", 29, 1.60],
    ["Ricardo", 31, 1.85],
    ["Patrícia", 26, 1.70],
    ["Gabriel", 24, 1.78],
    ["Juliana", 33, 1.68],
    ["Thiago", 21, 1.82],
    ["Larissa", 34, 1.64],
    ["Eduardo", 23, 1.77],
    ["Camila", 36, 1.66],
    ["André", 19, 1.79],
    ["Roberta", 38, 1.63],
    ["Felipe", 37, 1.81],
    ["Tatiane", 39, 1.67],
    ["Bruno", 40, 1.74],
    ["Aline", 41, 1.69],
    ["Rafael", 42, 1.76],
    ["Vanessa", 43, 1.72],
    ["Gustavo", 44, 1.78],
    ["Sabrina", 45, 1.71],
    ["Diego", 46, 1.80],
    ["Claudia", 47, 1.65],
    ["Leonardo", 48, 1.83],
    ["Juliana", 49, 1.70],
    ["Marcos", 50, 1.77],
    ["Ana", 51, 1.62],
    ["Robson", 52, 1.84],
    ["Juliana", 53, 1.66],
    ["Thiago", 54, 1.78],
    ["Larissa", 55, 1.69],
    ["Eduardo", 56, 1.75],
    ["Camila", 57, 1.68],
    ["André", 58, 1.80],
    ["Roberta", 59, 1.64],
    ["Felipe", 60, 1.82],
    ["Tatiane", 61, 1.67],
    ["Bruno", 62, 1.74],
    ["Aline", 63, 1.70],
    ["Rafael", 64, 1.76],
    ["Vanessa", 65, 1.72],
    ["Gustavo", 66, 1.78],
    ["Sabrina", 67, 1.71],
    ["Diego", 68, 1.80],
    ["Claudia", 69, 1.65],
    ["Leonardo", 70, 1.83],
    ["Juliana", 71, 1.70]   
]

nomeprocurado = input("Digite o nome que deseja procurar: ")
chaveprocura = 0
for vl in data:
    nome = vl[0]
    idade = vl[1]
    altura = vl[2]
    if (nomeprocurado == nome):
        print("DADOS ENCONTRADOS")
        print("Nome: ", nome)
        print("Idade: ", idade)
        print("Altura: ", altura)
        chaveprocura = 1
