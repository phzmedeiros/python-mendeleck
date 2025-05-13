from hashlib import algorithms_guaranteed
from statistics import median


dados={
       "JUVENAL"   : {"CELULAR":"991234567","EMAIL":"juvenal@gmailx.com","ALTURA":1.70,"PESO":80},
       "PERCIVAL"  : {"CELULAR":"994567897","EMAIL":"percival@gmailx.com","ALTURA":1.65,"PESO":90},
       "ADAMASTOR" : {"CELULAR":"991223231","EMAIL":"adamastor@gmailx.com","ALTURA":1.72,"PESO":88},
       "JUVENTINA" : {"CELULAR":"993422312","EMAIL":"juventina@gmailx.com","ALTURA":1.80,"PESO":72},
       "OMOPLATA"  : {"CELULAR":"923234554","EMAIL":"omoplata@gmailx.com","ALTURA":1.55,"PESO":65},
       }

# para acessar os dados de um dicionário, utilizamos a chave
# e não o índice, como em uma lista... Também podemos utilizar
# a chave de chave para acessar os dados de um dicionário de dicionários

for i in dados:
    print(i)
    print("\t CELULAR: ", dados[i]["CELULAR"]  )
    print("\t EMAIL: ",   dados[i]["EMAIL"]    )
    print("\t ALTURA: ",  dados[i]["ALTURA"]   )
    print("\t PESO: ",    dados[i]["PESO"],"\n")

while(True):
    print("\nSISTEMA TABAJARA - BIOMETRICO")
    print("1 - LISTAR")
    print("2 - CONSULTAR")
    print("3 - CADASTRAR")
    print("4 - DELETAR")
    print("5 - ALTERAR")
    print("6 - IMC")

    print("0 - SAIR")
    print("\n")
    opcao =input("DIGITE A SUA OPCAO: ")
    
    if (opcao=="0"):
        break
    
    if(opcao=="1"):
        print("\nLISTAR:")
        for i in dados:
            print(i)

    if(opcao=="2"):
        print("\nCONSULTAR:")
        nome = input("DIGITE O NOME: ")
        if nome in dados:
            print(nome)
            print("\t CELULAR: ", dados[nome]["CELULAR"]  )
            print("\t EMAIL: ",   dados[nome]["EMAIL"]    )
            print("\t ALTURA: ",  dados[nome]["ALTURA"]   )
            print("\t PESO: ",    dados[nome]["PESO"],"\n")
        else:
            print("NOME NÃO CADASTRADO.")

# # quem tem a maior altura
# # quem tem a menor altura
# # quem tem o maior peso
# # quem tem o menor peso
# # peso medio
# # altura media
# # o nome com maior numero de letras
# # o nome com menor numero de letras
# # calcular o imc
# # quem tem o maior imc
# # quem tem o menor imc