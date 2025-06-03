# -*- coding: utf-8 -*-
"""
Created on Wed May 21 11:16:22 2025
AULA20250521ARQUIVO004 B

ARQ20250521DATASET002.txt
@author: p226646
"""
#ABRIR O ARQUIVO PARA LEITURA
arquivo=open("ARQ20250521DATASET003.txt","r")

conteudo=arquivo.read()

arquivo.close()

dados=conteudo.split("\n")

DATASET004=[]

for pos in range(0,len(dados),2):
    aux=[dados[pos],int(dados[pos+1])]
    DATASET004.append(aux)

for i in DATASET004:
    print(i)

