# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:10:32 2025

@author: p226646
"""

#*********************************
#ALTERAR
#*********************************
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

nomeProcurado=input("DIGITE O NOME:  ")
chaveProcura=0
for pos,vl in enumerate(dados):
    nome=vl[0]
    idade=vl[1]
    altura=vl[2]
    if(nomeProcurado==nome):
        print("DADO CADASTRADOS:")
        print("NOME:    ",nome)
        print("IDADE:   ",idade)
        print("ALTURA:  ",altura)
        novoNome=input("DIGITAR NOVO NOME:   ")
        novoIdade=input("DIGITAR NOVA IDADE:  ")
        novoAltura=input("DIGITAR NOVA ALTURA: ")
        if (novoNome!=""):
            nome=novoNome
        if(novoIdade!=""):
            idade=int(novoIdade)
        if(novoAltura!=""):
            altura=float(novoAltura)
         
        #DEFINIR LISTA AUXILIAR
        aux=[nome,idade,altura]
        #ALTERAR REGISTRO NA POSICAO pos DO DATASET
        dados[pos]=aux
        
        chaveProcura=1
        
if (chaveProcura==0):
    print("\nNOME NAO CADASTRADO")
    
    
for vl in dados:
    print(vl)
    
    