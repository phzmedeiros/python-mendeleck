# -*- coding: utf-8 -*-
"""
Created on Wed May 14 10:05:52 2025
AULA20250514LISTAR B

@author: p226646
"""


dados={
       "JUVENAL":   {"CELULAR":"991234567","EMAIL":"juvenal@gmailx.com","ALTURA":1.70,"PESO":80},
       "PERCIVAL":  {"CELULAR":"994567897","EMAIL":"percival@gmailx.com","ALTURA":1.65,"PESO":90},
       "ADAMASTOR": {"CELULAR":"991223231","EMAIL":"adamastor@gmailx.com","ALTURA":1.72,"PESO":88},
       "JUVENTINA": {"CELULAR":"993422312","EMAIL":"juventina@gmailx.com","ALTURA":1.80,"PESO":72},
       "OMOPLATA":  {"CELULAR":"923234554","EMAIL":"omoplata@gmailx.com","ALTURA":1.55,"PESO":65},
       }

#LISTAR NOMES NO DATASET
#OS NOMES SAO OS INDEXADORES
print("\nLISTAR INDEXADORES:")
for i in dados:
    print(i)
    
#LISTAR O CONTEUDO DOS INDEXADORES
print("\nLISTAR TODOS OS DADOS")
for i in dados:
    aux=dados[i]
    celular=aux["CELULAR"]
    email=aux["EMAIL"]
    altura=aux["ALTURA"]
    peso=aux["PESO"]
    print("\nNOME:     ",i)
    print("CELULAR:  ",celular)
    print("EMAIL:    ",email)
    print("ALTURA:   ",altura)
    print("PESO:     ",peso)
    
    
#LISTAGEM ALTERNATIVA
print("\n\nLISTAGEM ALTERNATIVA COM 2 FOR")
for i in dados:
   print("\nNOME:     ",i)
   for j in dados[i]:
       print(j,":\t",dados[i][j])   
    


    
    
    




