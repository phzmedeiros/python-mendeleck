# -*- coding: utf-8 -*-
"""
Created on Wed May 21 10:12:03 2025
AULA20250521ARQUIVO001

ARQ20250521DATASET001.TXT
@author: p226646
"""

#ABRIR ARQUIVO PARA LEITURA
arquivo=open("ARQ20250521DATASET001.TXT","r")

#LER TODOS OS DADOS DO ARQUIVO
conteudo=arquivo.read()

#FECHAR ARQUIVO
arquivo.close()

#RECORTAR/SEPARAR OS REGISTROS
dados=conteudo.split("\n")

#CONVERTER OS REGISTROS EM INTEIRO
DATASET001=[]
for i in dados:
    aux=int(i)
    DATASET001.append(aux)

for i in DATASET001:
    print(i)
