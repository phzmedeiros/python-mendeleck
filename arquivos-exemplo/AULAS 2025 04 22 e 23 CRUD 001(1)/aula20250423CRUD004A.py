# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:20:53 2025

@author: p226646
"""

#********************************
#ALTERAR
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
for  pos,vl in enumerate(dados):
    nome=vl[0]
    idade=vl[1]
    altura=vl[2]
    if(nome==nomeProcurado):
        print("\nDADOS ENCONTRADOS - REGISTRO: ",pos)
        print("NOME:    ",nome)
        print("IDADE:   ",idade)
        print("ALTURA:  ",altura)
        novoNome=  input("DIGITAR NOVO NOME:   ")
        if (novoNome!=""):
            nome=novoNome
            
        novoIdade= input("DIGITAR NOVA IDADE:  ")
        if (novoIdade!=""):
            idade=int(novoIdade)
            
        novoAltura=input("DIGITAR NOVA ALTURA: ")
        if (novoAltura!=""):
            altura=float(novoAltura)
        
        aux=[nome,idade,altura]
        dados[pos]=aux
        chaveProcura=1

if(chaveProcura==0):
     print("NOME NAO CADASTRADO") 
     
     
     
for vl in dados:
    print(vl)