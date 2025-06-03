# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

#LISTAR OS DADOS
print("\nLISTAR DADOS CADASTRADOS")
tam=len(dados)
for pos in range(0,tam):
    print(pos,"\t",dados[pos])

print("\nLISTAR DADOS CADASTRADOS V2")
tam=len(dados)
for vl in dados:
    print(vl)

print("\nLISTAR DADOS CADASTRADOS V3")
tam=len(dados)
for pos,vl in enumerate(dados):
    print(pos,"\t",vl)

#CADASTRAR DADOS NO DATASET
nome="BEETHOR"
idade=5
altura=0.67
aux=[nome,idade,altura]
#ACRESCENTAR/CADFASTRAR NOVO REGISTRO
dados.append(aux)

#CADASTRAR DADOS NO DATASET
nome="PYTHOR"
idade=5
altura=0.67
aux=[nome,idade,altura]
#ACRESCENTAR/CADFASTRAR NOVO REGISTRO
dados.append(aux)

#LER OS DADOS DE NOME,IDADE,ALTURA
#CADASTRAR NO DATASET e LISTAR
# TODOS OS DADOS
nome=input("DIGITE O NOME: ")
idade=int(input("DIGITE IDADE:  "))
altura=float(input("DIGITE ALTURA: "))
aux=[nome,idade,altura]
dados.append(aux)

print("\nLISTAR DADOS CADASTRADOS V4")
tam=len(dados)
for pos,vl in enumerate(dados):
    print(pos,"\t",vl)









