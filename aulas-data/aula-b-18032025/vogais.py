frase = "O RATO ROEU A ROUPA DO REIZ DE RAPIDOPOLIS"
NCHAR = len(frase)

contador_vogais = 0
contador_espacos = 0
contador_consoantes = 0
pos = 0

while pos < NCHAR:
    if frase[pos] == ' ':
        contador_espacos = contador_espacos + 1
    elif frase[pos] == 'A' or frase[pos] == 'E' or frase[pos] == 'I' or frase[pos] == 'O' or frase[pos] == 'U':
        contador_vogais = contador_vogais + 1
    else:
        contador_consoantes += 1
    pos = pos + 1

print("Número de vogais: ", contador_vogais)
print("Número de espaços em branco: ", contador_espacos)
print("Número de consoantes: ", contador_consoantes)
print("Número de caracteres: ", NCHAR)