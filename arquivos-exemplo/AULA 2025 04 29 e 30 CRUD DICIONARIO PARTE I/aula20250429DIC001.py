# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

dicio={ "JUVENAL": "999125699",
        "PERITONIO": "999237879",
        "ESPATULA": "981224569",
             }

#LISTAR AS CHAVES INDEXADORAS DO DICIONARIO
for i in dicio:
    print(i)
    
#LISTAR O CONTEUDO EM dicio
for i in dicio:
    print(i,"\t",dicio[i])
    
   
#CONSULTAR
print("\nCONSULTA AO DICIONARIO")
nomeProc=input("DIGITE O NOME:  ")
try:
 print(nomeProc,"\t",dicio[nomeProc])
except:
    print("NOME NAO CADASTRADO")

#CADASTRAR
print("\nCADASTRAR:")
nome=input("DIGITE O NOME:  ")
celular=input("DIGITE CELULAR: ")
dicio[nome]=celular

for i in dicio:
    print(i,"\t",dicio[i]) 

#ALTERAR
print("\nALTERAR:")
nomeProc=input("DIGITE O NOME:  ")
try:
 print(nomeProc,"\t",dicio[nomeProc])
 novoCelular=input("DIGITE O NOVO CELULAR:")
 dicio[nomeProc]=novoCelular
except:
    print("NOME NAO CADASTRADO")

for i in dicio:
    print(i,"\t",dicio[i]) 

#DELETAR UM ITEM DO CICIOMARIO
print("\nDELETAR ITEM DICIONARIO")
nomeProc=input("DIGITE O NOME:  ")
try:
 print(nomeProc,"\t",dicio[nomeProc])
 dicio.pop(nomeProc)
except:
    print("NOME NAO CADASTRADO")

print("\nDICIONARIO ATUALIZADO")
for i in dicio:
    print(i,"\t",dicio[i]) 
    





    
    
    
    








