# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:51:00 2025

@author: p226646
"""

dicio={ "JUVENAL": "999125699",
        "PERITONIO": "999237879",
        "ESPATULA": "981224569",
        "ANTIMONIO":"3755455644",
        "BAROLLO":"333321231",
        "HOMMOPLATAH":"993452312"
             }

#LISTAR AS CHAVES DO DICIONARIO
for i in dicio:
    print(i)
    
print("\n")
#LISTAR O CONTEUDO DAS CHAVES
for i in dicio:
    print(i,"\t",dicio[i])


#CONSULTAR
print("\nCONSULTAR TELEFONE")
nomeProc=input("DIGITAR NOME:  ")
chaveEncontrado=0
for i in dicio:
    if(nomeProc==i):
        print(i,"\t",dicio[i])
        chaveEncontrado=1

if (chaveEncontrado==0):
        print("NOME NAO CADASTRADO")  
        
print("\nCONSULTAR TELEFONE V2")
try:
    print("NOME: ",nomeProc,"\t",dicio[nomeProc])      
except:
    print("DESCULPE, NOME NAO ENCONTRADO")       

#CADASTRAR
print("\nCADASTRAR NOVO NOME CELULAR")
nome=   input("DIGITAR NOME:    ")
celular=input("DIGITAR CELULAR: ")
dicio[nome]=celular

print("\n")
#LISTAR O CONTEUDO DAS CHAVES
for i in dicio:
    print(i,"\t",dicio[i])
    
    
#ALTERAR
print("\nALTERAR CELULAR")
nomeProc=input("DIGITAR NOME:")
try:
    print("NOME: ",nomeProc,"\t",dicio[nomeProc])      
    novoCelular=input("DIGITAR NOVO CELULAR: ")
    dicio[nomeProc]=novoCelular
except:
    print("DESCULPE, NOME NAO ENCONTRADO")       

print("\n")
#LISTAR O CONTEUDO DAS CHAVES
for i in dicio:
    print(i,"\t",dicio[i])
    

#DELETAR
print("\nDELETAR CADASTRO")
nomeProc=input("DIGITAR NOME:")
try:
    print("NOME: ",nomeProc,"\t",dicio[nomeProc])      
    dicio.pop(nomeProc)
    print("CADASTRO REMOVIDO")
except:
    print("DESCULPE, NOME NAO ENCONTRADO")       

print("\n")
#LISTAR O CONTEUDO DAS CHAVES
for i in dicio:
    print(i,"\t",dicio[i])
    
