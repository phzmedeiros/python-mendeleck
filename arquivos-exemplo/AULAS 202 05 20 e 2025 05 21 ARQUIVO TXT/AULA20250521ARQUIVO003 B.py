# -*- coding: utf-8 -*-
"""
Created on Wed May 21 10:57:00 2025

AULA20250521ARQUIVO003 B

ARQ20250521DATASET002.txt

@author: p226646
"""
#ABRIR O ARQUIVO COM OS DADOS
#EFETUAR A LEITURA DOS DADOS LINHA POR LINHA
#CONVERTER OS VALORES PARA FLOAT
#CALCULAR A MEDIA

#ABRIR O ARQUIVO PARA LEITURA
arquivo=open("ARQ20250521DATASET002.txt","r")

DATASET003=[]
linha=" "
while (linha!=""):
    #EFETUAR A LEITURA DE UMA LINHA DE DADOS
    linha=arquivo.readline()
    
    if (linha!=""):
        #SEPARAR DADOS
        dados=linha.split("\n")
        
        #CONVERTER A STRING EM UM FLOAT
        valor=float(dados[0])
        #ARMAZENAR OS DADOS NO DATASET003
        DATASET003.append(valor)

arquivo.close()

soma=0
for i in DATASET003:
    soma=soma+i
    
media=soma/len(DATASET003)
print("\nMEDIA:  ",format(media,".2f"))





