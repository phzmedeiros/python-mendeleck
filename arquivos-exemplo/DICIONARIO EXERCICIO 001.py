# -*- coding: utf-8 -*-
"""
Created on Sun May 11 19:00:10 2025

@author: AM2
"""

dados={
       "JUVENAL":   {"CELULAR":"991234567","EMAIL":"juvenal@gmailx.com","ALTURA":1.70,"PESO":80},
       "PERCIVAL":  {"CELULAR":"994567897","EMAIL":"percival@gmailx.com","ALTURA":1.65,"PESO":90},
       "ADAMASTOR": {"CELULAR":"991223231","EMAIL":"adamastor@gmailx.com","ALTURA":1.72,"PESO":88},
       "JUVENTINA": {"CELULAR":"993422312","EMAIL":"juventina@gmailx.com","ALTURA":1.80,"PESO":72},
       "OMOPLATA":  {"CELULAR":"923234554","EMAIL":"omoplata@gmailx.com","ALTURA":1.55,"PESO":65},
       }

while(True):
    print("\nSISTEMA TABAJARA - BIOMETRICO")
    print("1 - LISTAR")
    print("2 - CONSULTAR")
    print("3 - CADASTRAR")
    print("4 - DELETAR")
    print("5 - ALTERAR")
    print("6 - IMC")

    print("0 - SAIR")
    print("\n")
    opcao =input("DIGITE A SUA OPCAO: ")
    
    if (opcao=="0"):
        break
    
    if(opcao=="1"):
        print("\nLISTAR:")
        for vl in dados:
            print(vl)
        
    if(opcao=="2"):
        try:
             print("\nCONSULTAR:")
             nomeProcurado=input("DIGITE O NOME:  ")
             print("NOME:    ",nomeProcurado)
             print("CELULAR: ",dados[nomeProcurado]["CELULAR"])
             print("EMAIL:   ",dados[nomeProcurado]["EMAIL"])
             print("ALTURA:  ",dados[nomeProcurado]["ALTURA"])
             print("PESO:    ",dados[nomeProcurado]["PESO"])
        except:
             print("\nNOME NAO CADASTRADO")
                    
    if(opcao=="3"):
        print("\nCADASTRAR:") 
        nome=   input("DIGITE O NOME:   ")
        celular=input("DIGITE CELULAR:  ")
        email=input("DIGITE EMAIL:    ")
        altura=float(input("DIGITE ALTURA:   "))
        peso=int(input("DIGITE A IDADE:  "))
        
        aux={"CELULAR":celular,"EMAIL":email,"ALTURA":altura,"PESO":peso}
        
        dados[nome]=aux
        print("DADOS CADSATRADOS")
        
    if(opcao=="4"):
        try:
             print("\nDELETAR:")   
             nomeProcurado=input("DIGITE O NOME:  ")
             print("NOME:    ",nomeProcurado)
             print("CELULAR: ",dados[nomeProcurado]["CELULAR"])
             print("EMAIL:   ",dados[nomeProcurado]["EMAIL"])
             print("ALTURA:  ",dados[nomeProcurado]["ALTURA"])
             print("PESO:    ",dados[nomeProcurado]["PESO"])
             st=input("\nDESEJA REALMENTE DELETAR <S/N>:  ")
             if (st=="S")or(st=="s"):
                 dados.pop(nomeProcurado)
        except:
             print("\nNOME NAO CADASTRADO")
              
    if(opcao=="5"):
        try:
             print("\nALTERAR:")   
             nomeProcurado=input("DIGITE O NOME:  ")
             print("NOME:    ",nomeProcurado)
             celular=dados[nomeProcurado]["CELULAR"]
             email=dados[nomeProcurado]["EMAIL"]
             altura=dados[nomeProcurado]["ALTURA"]
             peso=dados[nomeProcurado]["PESO"]
             
             print("\nCELULAR: ",dados[nomeProcurado]["CELULAR"])
             auxCelular=input("DIGITE NOVO CELULAR:  ")
             if(auxCelular!=""):
                 celular=auxCelular
             
             print("\nEMAIL:   ",dados[nomeProcurado]["EMAIL"])
             auxEmail=input("DIGITE NOVO EMAIL:    ")
             if(auxEmail!=""):
                 email=auxEmail
                 
             print("\nALTURA:  ",dados[nomeProcurado]["ALTURA"])
             auxAltura=float(input("DIGITE NOVA ALTURA:   "))
             if (auxAltura!=""):
                 altura=auxAltura
                 
             print("\nPESO:    ",dados[nomeProcurado]["PESO"])
             auxPeso=int(input("DIGITE NOVO PESO:     "))
             if (auxPeso!=""):
                 peso=auxPeso
                 
             aux={"CELULAR":celular,"EMAIL":email,"ALTURA":altura,"PESO":peso}
             dados[nomeProcurado]=aux
             
        except:
             print("\nNOME NAO CADASTRADO")
             

    if(opcao=="6"):
        try:
         print("\nCALCULAR IMC:")
         nomeProcurado=input("DIGITE O NOME:  ")
         print("NOME:    ",nomeProcurado)
         print("CELULAR: ",dados[nomeProcurado]["CELULAR"])
         print("EMAIL:   ",dados[nomeProcurado]["EMAIL"])
         print("ALTURA:  ",dados[nomeProcurado]["ALTURA"])
         print("PESO:    ",dados[nomeProcurado]["PESO"])
         imc=dados[nomeProcurado]["PESO"]/(dados[nomeProcurado]["ALTURA"]*dados[nomeProcurado]["ALTURA"])
         print("IMC:  ",format(imc,"6.2f"))
        except:
             print("\nNOME NAO CADASTRADO")