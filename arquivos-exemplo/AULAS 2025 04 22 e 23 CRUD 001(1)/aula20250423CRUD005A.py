# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:00:30 2025

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
    print("\n")
    print("0 - SAIR")
    opcao=input("\nDIGITE A SUA OPCAO: ")
    
    if(opcao=="0"):
        break
    
    if(opcao=="1"):
        print("\nLISTAR:")
        for vl in dados:
            print(vl)
    
    if(opcao=="2"):
        print("\nCONSULTAR")
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
        
    if(opcao=="3"):
        print("\nCADASTRAR")
        nome=input("DIGITE O NOME:   ")
        idade=int(input("DIGITE A IDADE:  "))
        altura=float(input("DIGITE A ALTURA: "))
        
        aux=[nome,idade,altura]
        
        dados.append(aux)
                
    if(opcao=="4"):
        print("\nDELETAR")
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
                dados.remove(vl)
                print("DADOS REMOVIDOS")
                chaveProcura=1
        
        if(chaveProcura==0):
             print("NOME NAO CADASTRADO") 

    if (opcao=="5"):
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



