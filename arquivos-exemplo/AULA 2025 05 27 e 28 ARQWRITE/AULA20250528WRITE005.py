# -*- coding: utf-8 -*-
"""
Created on Wed May 28 09:16:27 2025
AULA20250528WRITE005
@author: p226646
"""
dataset=[]

arq=open("ELETRO004.TXT","r")
auxArq=" "
while(auxArq!=""):
    auxArq=arq.readline()
    if(auxArq!=""):
        dados=auxArq.split("|")
        aux=[dados[0],float(dados[1]),float(dados[2])]
        dataset.append(aux)
        print("NOME:              ",dados[0])
        print("QUANTIDADE:        ",dados[1])
        print("PRECO UNITARIO:  R$",dados[2])

arq.close()


