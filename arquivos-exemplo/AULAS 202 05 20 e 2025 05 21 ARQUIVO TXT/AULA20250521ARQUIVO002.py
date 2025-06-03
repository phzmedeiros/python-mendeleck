# -*- coding: utf-8 -*-
"""
Created on Wed May 21 08:46:50 2025
AULA20250521ARQUIVO002
@author: p226646
"""

#LER AS NOTAS DOS ALUNOS DE CDIA
# ARMAZENADAS EM ARQUIVO
# E CALCULAR A MEDIA

#ABRIR O ARQUIVO PARA LEITURA
arquivo=open("ARQ20250521DATASET002.txt","r")

#EFETUAR A LEITURA DOS DADOS
conteudo=arquivo.read()

#FECHAR ARQUIVO
arquivo.close()

print("\nDADOS LIDOS:")
print(conteudo)

#SEPARAR OS REGISTROS
dados=conteudo.split("\n")

#CONVERTER OS DADOS DE STRING PARA FLOAT
DATASET001=[]
for i in dados:
    aux=float(i)
    DATASET001.append(aux)
    
#CALCULAR A MEDIA
soma=0
for i in DATASET001:
    soma=soma+i
media=soma/len(DATASET001)
print("\nMEDIA:  ",format(media,"6.2f"))



