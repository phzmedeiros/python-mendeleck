# -*- coding: utf-8 -*-
"""
Created on Tue May 13 08:33:03 2025

@author: p226646
"""

dados={
       "JUVENAL":   {"CELULAR":"991234567","EMAIL":"juvenal@gmailx.com","ALTURA":1.70,"PESO":80},
       "PERCIVAL":  {"CELULAR":"994567897","EMAIL":"percival@gmailx.com","ALTURA":1.65,"PESO":90},
       "ADAMASTOR": {"CELULAR":"991223231","EMAIL":"adamastor@gmailx.com","ALTURA":1.72,"PESO":88},
       "JUVENTINA": {"CELULAR":"993422312","EMAIL":"juventina@gmailx.com","ALTURA":1.80,"PESO":72},
       "OMOPLATA":  {"CELULAR":"923234554","EMAIL":"omoplata@gmailx.com","ALTURA":1.55,"PESO":65},
       }

try:
    nomeProcurado=input("DIGITAR NOME:")
    aux=dados[nomeProcurado]
    print("\nNOME:  ",nomeProcurado)
    celular=aux["CELULAR"]
    email=aux["EMAIL"]
    altura=aux["ALTURA"]
    peso=aux["PESO"]
    print("CELULAR: ",celular)
    print("EMAIL:   ",email)
    print("ALTURA:  ",altura)
    print("PESO:    ",peso)
except:
    print("NOME NAO CADASTRADO")


