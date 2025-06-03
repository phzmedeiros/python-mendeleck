# -*- coding: utf-8 -*-
"""
Created on Wed May 21 10:43:31 2025
AULA20250521ARQUIVO002 B

ARQ20250521DATASET002.txt

@author: p226646
"""
#ABRIR O ARQUIVO COM OS DADOS
#EFETUAR A LEITURA DOS DADOS
#CONVERTER OS VALORES PARA FLOAT
#CALCULAR A MEDIA

#ABRIR O ARQUIVO PARA LEITURA
arquivo=open("ARQ20250521DATASET002.txt","r")

#LER DADOS DO ARQUIVO
conteudo=arquivo.read()

#FECHAR ARQUUIVO
arquivo.close()

#SEPARAR/RECORTAR OS REGISTROS
dados=conteudo.split("\n")

DATASET002=[]
for i in dados:
    valor=float(i)
    DATASET002.append(valor)

soma=0
print("\nVALORES DE NOTA:")
for i in DATASET002:
    print(i)
    soma=soma+i

media=soma/len(DATASET002)
print("\nMEDIA: ",format(media,"6.2f"))
