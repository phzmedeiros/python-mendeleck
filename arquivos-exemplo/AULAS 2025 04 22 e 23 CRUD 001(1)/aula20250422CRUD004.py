# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:11:53 2025

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


#CONSULTAR POR NOME
print("\nALTERAR POR NOME:")
nomeProcurado=input("DIGITE O NOME: ")
#PERCORRER TODO O DATASET
#PROCURANDO O NOME DESEJADO
chaveProcura=0
for pos,vl in enumerate(dados):
    nome=vl[0]
    idade=vl[1]
    altura=vl[2]
    if (nomeProcurado==nome):
        print("DADOS ENCONTRADOS: ")
        print("NOME:   ",nome)
        print("IDADE:  ",idade)
        print("ALTURA: ",altura)
        chaveProcura=1
        print("\n")
        auxNome=  input("DIGITE NOVO NOME:   ")
        auxIdade= input("DIGITE NOVA IDADE:  ")
        auxAltura=input("DIGITE NOVA ALTURA: ")
        if(auxNome!=""):
            nome=auxNome
        if(auxIdade!=""):
            idade=int(auxIdade)
        if(auxAltura!=""):
            altura=float(auxAltura)
        aux=[nome,idade,altura]
        dados[pos]=aux
        print("DADOS ALTERADOS")
        
if (chaveProcura==0):
    print("NOME NAO CADASTRADO")
    
    
for vl in dados:
    print(vl)