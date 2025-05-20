arquivo = open('aulas-data/aula-l-20052025/AULA20250520ARQUIVO-002.txt', 'r')

aux = arquivo.read()

print(aux)

arquivo.close()

##############################################################################

print("\nAPRESENTAR VALORES NO CONSOLE E CALCULAR A MEDIA")

arquivo = open("aulas-data/aula-l-20052025/AULA20250520ARQUIVO-002.txt", "r")

aux = " "

soma = 0
cont = 0
while aux != "":
    aux = arquivo.readline()
    aux1 = aux.split("\n")
    if aux != "":
        print(aux1[0])
        soma = soma + int(aux1[0])
        cont = cont + 1

media = soma / cont
print(f"A média é: ", format(media, '.2f'))
arquivo.close()
##############################################################################