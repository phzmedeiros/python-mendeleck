# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:46:08 2025

@author: p226646
"""

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

while(True):
    print("\nSISTEMA TABAJARA - BIOMETRICO")
    print("1 - LISTAR")
    print("2 - CONSULTAR")
    print("3 - CADASTRAR")
    print("4 - DELETAR")
    print("5 - ALTERAR")

    print("0 - SAIR")
    print("\n")
    opcao =input("DIGITE A SUA OPCAO: ")
    
    if (opcao=="0"):
        break
    
    if(opcao=="1"):
        print("\nLISTAR:")
        for vl in dados:
            print(vl)
        
    if(opcao=="2"):
         print("\nCONSULTAR:")
         nomeProcurado=input("DIGITE O NOME:  ")
         chaveProcura=0
         for vl in dados:
             nome=vl[0]
             idade=vl[1]
             altura=vl[2]
             if(nomeProcurado==nome):
                 print("DADO CADASTRADOS:")
                 print("NOME:    ",nome)
                 print("IDADE:   ",idade)
                 print("ALTURA:  ",altura)
                 chaveProcura=1
                 
         if (chaveProcura==0):
             print("\nNOME NAO CADASTRADO")
        
    if(opcao=="3"):
        print("\nCADASTRAR:") 
        nome=input("DIGITE O NOME:   ")
        idade=int(input("DIGITE A IDADE:  "))
        altura=float(input("DIGITE ALTURA:   "))
        
        aux=[nome,idade,altura]
        
        dados.append(aux)
        print("DADOS CADSATRADOS")
        
    if(opcao=="4"):
        print("\nDELETAR:")   
        nomeProcurado=input("DIGITE O NOME:  ")
        chaveProcura=0
        for vl in dados:
             nome=vl[0]
             idade=vl[1]
             altura=vl[2]
             if(nomeProcurado==nome):
                 print("DADO CADASTRADOS:")
                 print("NOME:    ",nome)
                 print("IDADE:   ",idade)
                 print("ALTURA:  ",altura)
                 #DELETAR - REMOVER REGISTRO
                 dados.remove(vl)
                 chaveProcura=1
                 
        if (chaveProcura==0):
             print("\nNOME NAO CADASTRADO")
       
    if(opcao=="5"):
        print("\nALTERAR:")
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