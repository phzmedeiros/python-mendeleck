# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 08:49:14 2025

@author: p226646
"""

dicio={ "JUVENAL": "999125699",
        "PERITONIO": "999237879",
        "ESPATULA": "981224569",
             }

# DESENVOLVER UM CRUD PARA O CADASTRO DE 
# UM DICIONARIO PARA AGENDA DE TELEFONES 
# CELULARES:

# 1 - LISTAR
# 2 - CONSULTAR
# 3 - CADASTRAR
# 4 - ALTERAR
# 5 - DELETAR

# 0 - SAIR


while(True):
    print("\nAGENDA TELEFONICA")
    print("1 - LISTAR")
    print("2 - CONSULTAR")
    print("3 - CADASTRAR")
    print("4 - ALTERAR")
    print("5 - DELETAR")
    print("\n0 - SAIR")
    opcao=input("DIGITE A OPCAO: ")
    
    if (opcao=="0"):
        break
    
    if(opcao=="1"):
        print("\nLISTAR")
        for i in dicio:
          print(i,"\t",dicio[i])  
        
    if(opcao=="2"):
        print("\nCONSULTAR")
        nomeProc=input("DIGITE O NOME:  ")
        try:
         print(nomeProc,"\t",dicio[nomeProc])
        except:
            print("NOME NAO CADASTRADO")        
        
    if(opcao=="3"):
        print("\nCADASTRAR")        
        nome=input("DIGITE O NOME:  ")
        celular=input("DIGITE CELULAR: ")
        dicio[nome]=celular
        
    if(opcao=="4"):
        print("\nALTERAR")        
        nomeProc=input("DIGITE O NOME:  ")
        try:
         print(nomeProc,"\t",dicio[nomeProc])
         novoCelular=input("DIGITE O NOVO CELULAR:")
         dicio[nomeProc]=novoCelular
        except:
            print("NOME NAO CADASTRADO")
            
    if(opcao=="5"):
        print("\nDELETAR")
        nomeProc=input("DIGITE O NOME:  ")
        try:
         print(nomeProc,"\t",dicio[nomeProc])
         dicio.pop(nomeProc)
        except:
            print("NOME NAO CADASTRADO")       
        
        
        
        