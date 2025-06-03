# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#********************************
#CONSULTAR
#********************************
dados=[ 
       ["ADAMASTOR",63,1.75],
       ["LINDOMARIO",71,1.45],
       ["LUKAZ",19,1.72],
       ["JUVENTINA",90,1.45],
       ["ADERBAL",15,1.98],
       ["GUZT AWUZ",30,1.25],
       ["ANNE CLARE",20,1.67],   
       ["BEETHÓRYAH",18,1.86], 
       ["MANNUEUZ",16,1.64],
       ["PERYTHONYO",55,1.56],
       ["MARY LAURE",17,1.81]    
       ]

nomeProcurado=input("DIGITE O NOME: ")
chaveProcura=0
for  vl in dados:
    nome=vl[0]
    idade=vl[1]
    altura=vl[2]
    if(nome==nomeProcurado):
        print("\nDADOS ENCONTRADOS")
        print("NOME:    ",nome)
        print("IDADE:   ",idade)
        print("ALTURA:  ",altura)
        chaveProcura=1

if(chaveProcura==0):
     print("NOME NAO CADASTRADO")    
    
    
    




