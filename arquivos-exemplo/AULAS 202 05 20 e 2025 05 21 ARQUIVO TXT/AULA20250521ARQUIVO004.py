# -*- coding: utf-8 -*-
"""
Created on Wed May 21 09:34:59 2025
AULA20250521ARQUIVO003

ARQ20250521DATASET003.TXT
@author: p226646
"""
#ABRIR O ARQUIVO PARA LEITURA
arquivo=open("ARQ20250521DATASET003.txt","r")

#LER TODOS OS DADOS DO ARQUIVO
conteudo=arquivo.read()

#FFECHAR ARQUIVO
arquivo.close()

#SEPARAR OS REGISTROS
dados=conteudo.split("\n")

#DEFINIR O DATASET
DATASET001=[]

for pos in range(0,len(dados),2):
    aux=[dados[pos],float(dados[pos+1])]
    DATASET001.append(aux)

print("\nDATASET:")
print(DATASET001)
print("\nDATASET:")
for i in DATASET001:
    print(i)