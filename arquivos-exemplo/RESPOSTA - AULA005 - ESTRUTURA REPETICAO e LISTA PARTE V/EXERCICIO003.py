# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 21:22:56 2025

@author: AM2
"""

# A empresa TATU – Textual Analysis To Users 
# está solicitando a você que desenvolva uma 
# aplicação de software para ler uma frase, 
# através do teclado, e realize as seguintes 
# operações:
#
#   1)Contar o número de espaços em branco
#   2)Contar o número de vogais e consoantes
#   3)Contar o número TOTAL de caracteres especiais: “ , . # $ % ? ! “
#   4)Contar o número de ocorrência de cada vogal, ou seja, o número de “A”, “E”, “I”, “O” e “U”
#   5)Dados um caracter específico, contar o número de ocorrências. Por exemplo, contar o número de ocorrências da letra “M”

frase=input("DIGITE A FRASE - USAR LETRA MAIUSCULA: ")
caracterEspecifico=input("DIGITE UM CARACTER PARA BUSCA: ")

#caracterEspecifico="M"
#frase="O RATO DE RAPIDOPOLIS, MUITO FAMINTO, ROEU A ROUPA DO REI ?"

tam = len(frase)

somaBranco=0
somaVogal=0
somaConsoante=0
somaEspecial=0
somacaracterEspecifico=0

pos=0
while(pos<tam):
    #CONTAR VOGAL
    if ((frase[pos]=="A")or(frase[pos]=="E")or(frase[pos]=="I")or(frase[pos]=="O")or(frase[pos]=="U")):
        somaVogal=somaVogal+1

    #CONTAR BRANCO
    if (frase[pos]==" "):
        somaBranco=somaBranco+1

    #CONTAR ESPECIAL
    if ((frase[pos]==",")or(frase[pos]==".")or(frase[pos]=="#")or(frase[pos]=="$")or(frase[pos]=="%")or(frase[pos]=="?")or(frase[pos]=="!")):
        somaEspecial=somaEspecial+1

    #CONTAR CARACTER ESPECIFICO
    if (frase[pos]==caracterEspecifico):
        somacaracterEspecifico=somacaracterEspecifico+1

    pos=pos+1

#CALCULAR O NUMERO DE CONSOANTES    
somaConsoante=tam-somaBranco-somaConsoante-somaEspecial-somaVogal

print("\nFRASE: ",frase)


print("\nNUMERO TOTAL DE CARACTERES:     ",tam)
print("NUMERO DE CARACTERES ESPECIAIS: ",somaEspecial)
print("NUMERO DE ESPACOS EM BRANCO:    ",somaBranco)
print("NUMERO DE CONSOANTES:           ",somaConsoante)
print("NUMERO DE VOGAIS:               ",somaVogal)
print("NUMERO DE CARACTER ESPECIFICO [",caracterEspecifico,"]: ",somacaracterEspecifico)




