# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 08:08:58 2025

@author: p226646
"""

dicio={ "JUVENAL": "999125699",
        "PERITONIO": "999237879",
        "ESPATULA": "981224569",
             }

#LISTAR OS ROTULOS DE INDEXACAO
for i in dicio:
    print(i)

#LISTAR O CONTEUDO NO dicio
print("\nLISTAR O CONTEUDO DO DICIONARIO")
for i in dicio:
    print(i,"\t",dicio[i])

#CONSULTAR
print("\nCULSULTA TIPO 1 - BUSCAR DADOS")
nomeProc=input("DIGITE O NOME: ")
chaveProcura=0
for i in dicio:
    if (i==nomeProc):
        print("NOME: ",i,"\t",dicio[i])
        chaveProcura=1
        break
   
if (chaveProcura==0):
        print("NOME NAO CADASTRADO")
        
print("\nCULSULTA TIPO 2 - BUSCAR DIRETA")
try:
   print("NOME: ",nomeProc,"\t",dicio[nomeProc])
except:
    print("NOME NAO CADASTRADO !!!!!! ")


#CADASTRAR
print("\nCADASTRANDO DADOS:")
nome=   input("DIGITE NOME:    ")
celular=input("DIGITE CELULAR: ")
dicio[nome]=celular

print(" ")
for i in dicio:
    print(i,"\t",dicio[i])
    

#ALTERAR
print("\nALTERANDO DADOS:")
nomeProc=input("DIGITE O NOME: ")
try:
   print("NOME: ",nomeProc,"\t",dicio[nomeProc])
   novoCelular=input("DIGITE NOVO CELULAR:")
   dicio[nomeProc]=novoCelular
except:
    print("NOME NAO CADASTRADO !!!!!! ")

print(" ")
for i in dicio:
    print(i,"\t",dicio[i])


#DELETAR
print("\nDELETANDO UM CADASTRO:")
nomeProc=input("DIGITE O NOME: ")
try:
   print("NOME: ",nomeProc,"\t",dicio[nomeProc])
   dicio.pop(nomeProc)
   print("CADASTRO REMOVIDO")
except:
    print("NOME NAO CADASTRADO !!!!!! ")


print(" ")
for i in dicio:
    print(i,"\t",dicio[i])
    
    
