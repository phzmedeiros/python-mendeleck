# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:00:30 2025
ADAMASTOR
63
1.75
LINDOMARIO
71
1.45
LUKAZ
19
1.72
JUVENTINA
90
1.45
ADERBAL
15
1.98
GUZT AWUZ
30
1.25
ANNE CLARE
20
1.67
BEETHÓRYAH
18
1.86
MANNUEUZ
16
1.64
PERYTHONYO
55
1.56
MARY LAURE
17
1.81

@author: p226646
"""

dados=[   ]

while(True):
    print("\nSISTEMA TABAJARA - BIOMETRICO")
    print("1 - LISTAR")
    print("2 - CONSULTAR")
    print("3 - CADASTRAR")
    print("4 - DELETAR")
    print("5 - ALTERAR")
    print("6 - LER DADOS DO ARQUIVO")
    print("7 - GRAVAR DADOS NO ARQUIVO")
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


    if (opcao=="6"):
        try:
            #LENDO OS DADOS GRAVADOS
            arquivo = open('EXEMPLOTXTCRUD001.txt', 'r')    
            flagFImArquivo=" "
            while (flagFImArquivo!=""):
           
                nome = arquivo.readline()
                flagFImArquivo=nome
                nome=nome.split("\n")
                
                idade = arquivo.readline()
                idade=idade.split("\n")
                
                altura = arquivo.readline()
                altura=altura.split("\n")

                if (nome[0]!=""):
                    aux=[nome[0],int(idade[0]),float(altura[0])]
                    dados.append(aux)
            print("LEITURA DE DADOS EFETUADA COM SUCESSO")       
        except:
             print("ERRO DE LEITURA")
        arquivo.close()
        
    if (opcao=="7"):
        try:
            #GRAVANDO OS DADOS GRAVADOS
            arquivo = open('EXEMPLOTXTCRUD001.txt', 'w')    
            for i in dados:
                arquivo.writelines(i[0]+"\n")
                arquivo.writelines(format(i[1],"d")+"\n")
                arquivo.writelines(format(i[2],".2f")+"\n")
            print("ESCRITA DE DADOS EFETUADA COM SUCESSO")       
        except:
             print("ERRO DE ESCRITA")
        arquivo.close()
        
        
        
        
        