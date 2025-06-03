# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 09:06:26 2025

@author: p226646
"""

dados=[ 
       ["ADAMASTOR",18,1.70],
       ["LUKAZ",19,1.72],
       ["JUVENTINA",90,1.45],
       ["ADERBAL",15,1.98],
       ["BYTHOR",30,1.25],
       ["LAWRAZ",20,1.67],   
       ["BEETHÓRYAH",18,1.86], 
       ["MANNUEU",16,1.64],
       ["PERYTHONYO",55,1.56],
       ["JYUWANYX",17,1.81]
       ]

#ACESSAR CAMPOS ESPECIFICOS DE
# UM DATASET
print("\nLISTAR CAMPOS  V1")
for vl in dados:
    #IMPRIMIR O REGISTRO
    print(vl)
    #ACESSO AOS CAMPOS DE UM REGISTRO
    nome=vl[0]
    idade=vl[1]
    altura=vl[2]
    print("NOME:   ",nome)
    print("IDADE:  ",idade)
    print("ALTURA: ",altura)
    print("\n")
    
#DESENVOLVER UMA APLICACAO DE SOFTWARE
#PARA CALCULAR A IDADE MEDIA 
print("\nCALCULAR A IDADE E ALTURA MEDIA:")
somaIdade=0
somaAltura=0
for vl in dados:
    somaIdade=somaIdade+vl[1]
    somaAltura=somaAltura+vl[2]

mediaIdade=somaIdade/len(dados)
mediaAltura=somaAltura/len(dados)
print("IDADE MEDIA:  ",format(mediaIdade,"6.2f"))
print("ALTURA MEDIA: ",format(mediaAltura,"6.2f"))

#DESENVOLVER UMA APLICACAO DE SOFTWARE
#BASEADO NO CODIGO ANTERIOR
#PARA INDICAR A MAIOR E A MENOR IDADE
#PARA INDICAR A MAIOR E A MENOR ALTURA
#PARA INDICAR A PESSOA COM MAIOR IDADE
#PARA INDICAR A PESSOA COM MENOR IDADE
#PARA INDICAR A PESSOA COM MAIOR ALTURA
#PARA INDICAR A PESSOA COM MENOR ALTURA
#DESENVOLVER UMA APLICACAO DE SOFTWARE
#PARA CALCULAR A IDADE MEDIA 
print("\nCALCULAR A IDADE E ALTURA MEDIA - MAXIMA - MINIMA:")
somaIdade=0
maiorIdade=-100000
nomemaiorIdade=""
menorIdade=1000000
nomemenorIdade=""
somaAltura=0
maiorAltura=-100000
nomemaiorAltura=""
menorAltura=1000000
nomemenorAltura=""
for vl in dados:
    somaIdade=somaIdade+vl[1]
    if (vl[1]>maiorIdade):
        maiorIdade=vl[1]
        nomemaiorIdade=vl[0]
    if (vl[1]<menorIdade):
        menorIdade=vl[1]
        nomemenorIdade=vl[0]
        
    somaAltura=somaAltura+vl[2]
    if (vl[2]>maiorAltura):
        maiorAltura=vl[2]
        nomemaiorAltura=vl[0]
    if (vl[2]<menorAltura):
        menorAltura=vl[2]
        nomemenorAltura=vl[0]
        
mediaIdade=somaIdade/len(dados)
mediaAltura=somaAltura/len(dados)
print("IDADE MEDIA:  ",format(mediaIdade,"6.2f"))
print("PESSOA MAIOR IDADE: ",nomemaiorIdade)
print("MAIOR IDADE:  ",format(maiorIdade,"6.2f"))
print("PESSOA MENOR IDADE: ",nomemenorIdade)
print("MENOR IDADE:  ",format(menorIdade,"6.2f"))
print("ALTURA MEDIA: ",format(mediaAltura,"6.2f"))
print("PESSOA MAIOR ALTURA: ",nomemaiorAltura)
print("MAIOR ALTURA: ",format(maiorAltura,"6.2f"))
print("PESSOA MENOR ALTURA: ",nomemenorAltura)
print("MENOR ALTURA  ",format(menorAltura,"6.2f"))

print('\n')
print("*"*47 )
print("PRINT ALTERNATIVO:\n")
print("IDADE MEDIA:  ",format(mediaIdade,"6.2f"))
print("PESSOA MAIOR IDADE: ",nomemaiorIdade,"  ",format(maiorIdade,"6.2f")," ANOS")
print("PESSOA MENOR IDADE: ",nomemenorIdade,format(menorIdade,"6.2f")," ANOS")

print("\nALTURA MEDIA: ",format(mediaAltura,"6.2f"))
print("PESSOA MAIOR ALTURA: ",nomemaiorAltura,format(maiorAltura,"6.2f")," metros")
print("PESSOA MENOR ALTURA: ",nomemenorAltura,format(menorAltura,"6.2f")," metros")
