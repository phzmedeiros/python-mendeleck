# -*- coding: utf-8 -*-
"""
Created on Wed May 21 09:14:24 2025
AULA20250521ARQUIVO003

@author: p226646
"""
#EFETUAR A LEITURA DOS DADOS 
# DE UM ARQUIVO, LINHA POR LINHA

#ABRIR O ARQUIVO PARA LEITURA
arquivo=open("ARQ20250521DATASET002.txt","r")

DATASET001=[]

aux=" "
cont=0
while (aux!=""):
    #EFETUAR A LEITURA DE UMA LINHA
    aux=arquivo.readline()
    if (aux!=""):
        #REMOVER O \n
        aux2=aux.split("\n")
        #CONVERTER A PRIMEIRA POSICAO DE aux2
        # EM UM NUMERO float
        valor=float(aux2[0])
        #ARMAZENAR O valor NO DATASET001
        DATASET001.append(valor)
        cont=cont+1
        
print("NO ARQUIVO EXISTEM ",cont," NOTAS")
print("NOTAS:")
for i in DATASET001:
    print(i)











