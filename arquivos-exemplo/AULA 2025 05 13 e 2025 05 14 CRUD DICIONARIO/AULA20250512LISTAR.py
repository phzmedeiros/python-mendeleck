# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



dados={
       "JUVENAL":   {"CELULAR":"991234567","EMAIL":"juvenal@gmailx.com","ALTURA":1.70,"PESO":80},
       "PERCIVAL":  {"CELULAR":"994567897","EMAIL":"percival@gmailx.com","ALTURA":1.65,"PESO":90},
       "ADAMASTOR": {"CELULAR":"991223231","EMAIL":"adamastor@gmailx.com","ALTURA":1.72,"PESO":88},
       "JUVENTINA": {"CELULAR":"993422312","EMAIL":"juventina@gmailx.com","ALTURA":1.80,"PESO":72},
       "OMOPLATA":  {"CELULAR":"923234554","EMAIL":"omoplata@gmailx.com","ALTURA":1.55,"PESO":65},
       }

#LISTAR OS ROTULOS - INDEXADORES
for i in dados:
    print(i)

#LISTAR O CONTEUDO DE UMA LISTA
print("\nLISTAR CONTEUDO DA LISTA:")
#A VARIAVEL i EH O INDEXADOR PARA
#ACESSO AO DICIONARIO
for i in dados:
    #SEPARAR OS DADOS REFERENTES
    #A PESSOA i
    aux=dados[i]
    print("\nNOME:  ",i)
    celular=aux["CELULAR"]
    email=aux["EMAIL"]
    altura=aux["ALTURA"]
    peso=aux["PESO"]
    print("CELULAR: ",celular)
    print("EMAIL:   ",email)
    print("ALTURA:  ",altura)
    print("PESO:    ",peso)
    


