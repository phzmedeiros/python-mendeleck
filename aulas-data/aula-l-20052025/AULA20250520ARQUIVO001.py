arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-001.txt", "r")

aux = " "

while aux != "":
    aux = arquivo.readline()
    print(aux, end="")

arquivo.close()

#############################################################################

print("\nPRIMEIRA FORMA DE LER UM ARQUIVO")
# A primeira forma de ler um arquivo é utilizando o método read()
arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-001.txt", "r")

aux0 = arquivo.read()

print(aux0)

arquivo.close()

#############################################################################

print("\nSEGUNDA FORMA DE LER UM ARQUIVO")
# A segunda forma de ler um arquivo é utilizando o método readlines()
arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-001.txt", "r")

aux = " "

while aux != "":
    aux = arquivo.readline()
    aux1 = aux.split("\n")
    print(aux1[0])

arquivo.close()

#############################################################################