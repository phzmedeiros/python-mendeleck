# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 08:44:55 2025

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

#*****************************
#CRUD COMPLETO COM MENU
#*****************************
while (True):
    print("\nSISTEMA TABAJARA - BIOMETRICO")
    print("1 - CADASTRAR")
    print("2 - LISTAR")
    print("3 - CONSULTAR")
    print("4 - DELETAR")
    print("5 - ALTERAR")
    print("  ")
    print("0 - SAIR")
    opcao=input("\nDIGITE A SUA OPCAO: ")

    if (opcao=="0"):
        break

    if (opcao=="1"):
        print("\nCADASTRAR DADOS:")
        nome= input("DIGITE O NOME:  ")
        idade=int(input("DIGITE IDADE:   "))
        altura=float(input("DIGITE ALTURA:  "))
        
        aux=[nome,idade,altura]
        
        #ACRESCENTAR NO FINAL DO DATASET
        dados.append(aux)
        print("DADOS CADASTRADOS")

    if (opcao=="2"):
        print("\nLISTAR DADOS:")
        for vl in dados:
            print(vl)

    if (opcao=="3"):
        print("\nCONSULTAR POR NOME:")
        nomeProcurado=input("DIGITE O NOME: ")
        #PERCORRER TODO O DATASET
        #PROCURANDO O NOME DESEJADO
        chaveProcura=0
        for vl in dados:
            nome=vl[0]
            idade=vl[1]
            altura=vl[2]
            if (nomeProcurado==nome):
                print("DADOS ENCONTRADOS: ")
                print("NOME:   ",nome)
                print("IDADE:  ",idade)
                print("ALTURA: ",altura)
                chaveProcura=1
                
        if (chaveProcura==0):
            print("NOME NAO CADASTRADO")

    if (opcao=="4"):
        print("\nDELETAR POR NOME:")
        nomeProcurado=input("DIGITE O NOME: ")
        #PERCORRER TODO O DATASET
        #PROCURANDO O NOME DESEJADO
        chaveProcura=0
        for vl in dados:
            nome=vl[0]
            idade=vl[1]
            altura=vl[2]
            if (nomeProcurado==nome):
                print("DADOS ENCONTRADOS: ")
                print("NOME:   ",nome)
                print("IDADE:  ",idade)
                print("ALTURA: ",altura)
                #REMOVER DO DATASET
                dados.remove(vl)
                print("DADOS REMOVIDOS")
                chaveProcura=1
                
        if (chaveProcura==0):
            print("NOME NAO CADASTRADO")
  
    if(opcao=="5"):
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
        
        
        