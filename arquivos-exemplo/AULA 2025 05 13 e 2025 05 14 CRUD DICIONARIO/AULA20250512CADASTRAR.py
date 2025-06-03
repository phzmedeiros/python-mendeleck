# -*- coding: utf-8 -*-
"""
Created on Tue May 13 08:48:33 2025

@author: p226646
"""



dados={
       "JUVENAL":   {"CELULAR":"991234567","EMAIL":"juvenal@gmailx.com","ALTURA":1.70,"PESO":80},
       "PERCIVAL":  {"CELULAR":"994567897","EMAIL":"percival@gmailx.com","ALTURA":1.65,"PESO":90},
       "ADAMASTOR": {"CELULAR":"991223231","EMAIL":"adamastor@gmailx.com","ALTURA":1.72,"PESO":88},
       "JUVENTINA": {"CELULAR":"993422312","EMAIL":"juventina@gmailx.com","ALTURA":1.80,"PESO":72},
       "OMOPLATA":  {"CELULAR":"923234554","EMAIL":"omoplata@gmailx.com","ALTURA":1.55,"PESO":65},
       }

while True:
    try:
        nome=   input("DIGITAR NOME:    ")
        celular=input("DIGITAR CELULAR: ")
        email=  input("DIGITAR EMAIL:   ")
        altura=float( input("DIGITAR ALTURA:  "))
        peso= int( input("DIGITAR PESO:    "))
        
        aux={"CELULAR":celular,
             "EMAIL":email,
             "ALTURA":altura,
             "PESO":peso}
        
        dados[nome]=aux
        break
    except:
        print("ATENCAO: POR FAVOR, DIGITAR SOMENTE NUMEROS")









