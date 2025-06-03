# -*- coding: utf-8 -*-
"""
Created on Wed May 14 09:29:20 2025
AULA20250514ALTERAR
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
        print("\nALTERAR POR NOME:")
        nomeProcurado=input("DIGITE O NOME: ")
        aux=dados[nomeProcurado]
        celular=aux["CELULAR"]
        email=aux["EMAIL"]
        altura=aux["ALTURA"]
        peso=aux["PESO"]
        print("\nNOME:     ",nomeProcurado)
        print("CELULAR:  ",celular)
        print("EMAIL:    ",email)
        print("ALTURA:   ",altura)
        print("PESO:     ",peso)        
        op=input("DESEJA REALMENTE ALTERAR <S/N> ? ")
        if (op=="S")or(op=="s"):
            novocelular=input("DIGITAR NOVO CELULAR:  ")
            if (novocelular!=""):
                celular=novocelular
                
            novoemail=  input("DIGITAR NOVO EMAIL:    ")
            if (novoemail!=""):
                email=novoemail
                
            novaaltura=input("DIGITAR NOVA ALTURA:   ")
            if(novaaltura!=""):
                altura=float(novaaltura)
                
            novopeso= input("DIGITAR NOVO PESO:     ")
            if(novopeso!=""):
                peso=int(novopeso)
                
            aux={"CELULAR":celular,
                 "EMAIL":email,
                 "ALTURA":altura,
                 "PESO":peso}
            dados[nomeProcurado]=aux
        break
    except:
        print("DIGITAR SOMENTE VALORES NUMERICOS")
