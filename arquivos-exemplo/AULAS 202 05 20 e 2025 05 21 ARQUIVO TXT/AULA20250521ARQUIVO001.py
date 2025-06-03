# -*- coding: utf-8 -*-
"""
Spyder Editor
ARQ20250521DATASET002.TXT

ARQ20250521DATASET001.txt

AULA20250521ARQUIVO001
This is a temporary script file.
"""

#LER OS DADOS DE UM ARQUIVO
# E APRESENTAR OS VALORES 
# NO DISPLAY

arquivo=open("ARQ20250521DATASET001.txt","r")

#LER TODOS OS DADOS DO ARQUIVO
conteudo=arquivo.read()

arquivo.close()

print(conteudo)

#SEPARAR OS REGISTROS
dados=conteudo.split("\n")

#CONVERTER OS DADOS DOS REGISTROS
#EM UM VALOR INTEIRO
auxDados=[]
for i in dados:
    aux=int(i)
    auxDados.append(aux)



