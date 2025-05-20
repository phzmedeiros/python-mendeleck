# ler o arquivo AULA20250520ARQUIVO-003.txt
# LER NOME E IDADE
# APRESENTAR VALORES NO CONSOLE E CALCULAR A MEDIA
# CRIAR UM DATASET

print("\nMEDIA DAS IDADES")

arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-003.txt", "r")
dados = []
soma = 0
cont = 0
auxNome = " "
auxIdade = " "

while auxNome != "":
    auxNome = arquivo.readline()
    aux = auxNome.split("\n")
    nome = aux[0]

    auxIdade = arquivo.readline()
    aux = auxIdade.split("\n")
    if auxNome != "":
        cont = cont + 1
        idade = int(aux[0])
        soma = soma + idade
        print(nome,"\t", idade)
        aux2 = [nome, idade]
        dados.append(aux2)
arquivo.close()

media = soma / cont
print("A média das idades é: ", format(media, ".2f"))
print("\nDATASET")
print(dados)