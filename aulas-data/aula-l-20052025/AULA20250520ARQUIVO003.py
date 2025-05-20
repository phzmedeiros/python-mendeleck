# LER O ARQUIVO: AULA20250520ARQUIVO-003.txt
# CONTENDO NOME E IDADE
# APRESENTAR VALORES NO CONSOLE E CALCULAR A MEDIA

print("\nLEITURA DOS DADOS")
arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-003.txt", "r")

auxNome = " "
auxIdade = " "

while auxNome != "":
    auxNome = arquivo.readline()
    auxIdade = arquivo.readline()
    print(auxNome,"\t", auxIdade)

arquivo.close()

#############################################################################

print("\nLEITURA DOS DADOS")
arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-003.txt", "r")

auxNome = " "
auxIdade = " "

while auxNome != "":
    auxNome = arquivo.readline()
    aux = auxNome.split("\n")
    nome = aux[0]
    
    auxIdade = arquivo.readline()
    aux = auxIdade.split("\n")
    if auxNome != "":
        idade = int(aux[0])
        print(nome,"\t", idade)

arquivo.close()

#############################################################################

print("\nMEDIA DAS IDADES")

arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-003.txt", "r")

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
media = soma / cont
print("A média das idades é: ", format(media, ".2f"))
arquivo.close()

#############################################################################

