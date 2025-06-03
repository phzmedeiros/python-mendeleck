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
    print("7 - ESTATISTICAS")

    print("0 - SAIR")
    print("\n")
    opcao =input("DIGITE A SUA OPCAO: ")
    
    if (opcao=="0"):
        break
    
    #LISTAR
    if(opcao=="1"):
        print("\nLISTAR:")
        for vl in dados:
            print(vl)
    
    #CONSULTAR
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
                    
    #CADASTRAR         
    if(opcao=="3"):
        print("\nCADASTRAR:") 
        nome=   input("DIGITE O NOME:   ")
        celular=input("DIGITE CELULAR:  ")
        email=input("DIGITE EMAIL:    ")
        altura=float(input("DIGITE ALTURA:   "))
        peso=int(input("DIGITE A IDADE:  "))
        st=input("DESEJA REALMENTE CADASTRAR <S/N> ? ")
        if (st=="S")or(st=="s"):
            aux={"CELULAR":celular,"EMAIL":email,"ALTURA":altura,"PESO":peso}
            dados[nome]=aux
            print("DADOS CADASTRADOS")
        else:
            print("DADOS NAO CADASTRADOS")
        
    #DELETAR    
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
                 print("DADOS DELETADOS")
        except:
             print("\nNOME NAO CADASTRADO")
              
    #ALTERAR         
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
             
             st=input("\nDESEJA REALMENTE ALTERAR OS DADOS <S/N>:  ")
             if (st=="S")or(st=="s"):
                    aux={"CELULAR":celular,"EMAIL":email,"ALTURA":altura,"PESO":peso}
                    dados[nomeProcurado]=aux
                    print("DADOS DELETADOS")
        except:
             print("\nNOME NAO CADASTRADO")
             
    #CALCULO DO IMC INDIVIDUAL
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
             
    #ESTATISTICAS         
    if(opcao=="7"):
        print("\nESTATISTICAS:")
        #*****************************************
        #   INDICAR A PESSOA COM A MAIOR ALTURA
        #*****************************************
        maiorAltura=-1000
        maiorAlturaNome=""
        #SEPARAR OS INDEXADORES
        for i in dados:
            #VERIFICAR A MAIOR ALTURA
            if (dados[i]["ALTURA"]>maiorAltura):
                maiorAltura=dados[i]["ALTURA"]
                maiorAlturaNome=i    
        #IMPRIMIR O RESULTADO
        print("MAIOR ALTURA:  ",format(maiorAlturaNome,"20s"),format(maiorAltura,"10.2f"))
        
        #*****************************************
        #   INDICAR A PESSOA COM A MENOR ALTURA
        #*****************************************
        menorAltura=1000
        menorAlturaNome=""
        #SEPARAR OS INDEXADORES
        for i in dados:
            #VERIFICAR A MENOR ALTURA
            if (dados[i]["ALTURA"]<menorAltura):
                menorAltura=dados[i]["ALTURA"]
                menorAlturaNome=i    
        #IMPRIMIR O RESULTADO
        print("MENOR ALTURA:  ",format(menorAlturaNome,"20s"),format(menorAltura,"10.2f"))
        
        #*****************************************
        #   INDICAR A PESSOA COM O MAIOR PESO
        #*****************************************
        maiorPeso=-1000
        maiorPesoNome=""
        #SEPARAR OS INDEXADORES
        for i in dados:
            #VERIFICAR O MAIOR PESO
            if (dados[i]["PESO"]>maiorPeso):
                maiorPeso=dados[i]["PESO"]
                maiorPesoNome=i    
        #IMPRIMIR O RESULTADO
        print("MAIOR PESO:    ",format(maiorPesoNome,"20s"),format(maiorPeso,"10.2f"))
        
        #*****************************************
        #   INDICAR A PESSOA COM O MENOR PESO
        #*****************************************
        menorPeso=1000
        menorPesoNome=""
        #SEPARAR OS INDEXADORES
        for i in dados:
            #VERIFICAR O MENOR PESO
            if (dados[i]["PESO"]<menorPeso):
                menorPeso=dados[i]["PESO"]
                menorPesoNome=i    
        #IMPRIMIR O RESULTADO
        print("MENOR PESO:    ",format(menorPesoNome,"20s"),format(menorPeso,"10.2f"))
        
        #*****************************************
        #   CALCULAR O PESO MÉDIO
        #*****************************************
        somaPeso=0
        tam=len(dados)
        #SEPARAR OS INDEXADORES
        for i in dados:
            somaPeso=somaPeso+dados[i]["PESO"]
        mediaPeso=somaPeso/tam    
        #IMPRIMIR O RESULTADO
        print("MEDIA PESO:  ...................... ",format(mediaPeso,"10.2f"))
        
        #*****************************************
        #   CALCULAR A ALTURA MÉDIA
        #*****************************************
        somaAltura=0
        tam=len(dados)
        #SEPARAR OS INDEXADORES
        for i in dados:
            somaAltura=somaAltura+dados[i]["ALTURA"]
        mediaAltura=somaAltura/tam    
        #IMPRIMIR O RESULTADO
        print("MEDIA ALTURA: ..................... ",format(mediaAltura,"10.2f"))
        
        #*****************************************
        #   O NOME COM MAIOR NÚMERO DE LETRAS
        #*****************************************
        maiorLetra=-1000
        maiorLetraNome=""
        #SEPARAR OS INDEXADORES
        for i in dados:
            #VERIFICAR O MAIOR PESO
            if (len(i)>maiorLetra):
                maiorLetra=len(i)
                maiorLetraNome=i    
        #IMPRIMIR O RESULTADO
        print("NOME MAIOR:    ",format(maiorLetraNome,"20s"),format(maiorLetra,"10.2f"))
        
        #*****************************************
        #   O NOME COM MENOR NÚMERO DE LETRAS
        #*****************************************
        menorLetra=1000
        menorLetraNome=""
        #SEPARAR OS INDEXADORES
        for i in dados:
            #VERIFICAR O MAIOR PESO
            if (len(i)<menorLetra):
                menorLetra=len(i)
                menorLetraNome=i    
        #IMPRIMIR O RESULTADO
        print("NOME MENOR:    ",format(menorLetraNome,"20s"),format(menorLetra,"10.2f"))
        
        #*****************************************
        #   CALCULAR O IMC DE TODOS OS CADASTROS
        #*****************************************
        maiorIMC=-100000
        maiorIMCNome=""
        menorIMC=100000
        menorIMCNome=""
        print("\nCALCULO DO IMC:")
        for i in dados:
            altura=dados[i]["ALTURA"]
            peso=dados[i]["PESO"]
            imc=peso/(altura*altura)
            print(format(i,"20s"),format(imc,"10.2f"))
            if(imc>maiorIMC):
                maiorIMC=imc
                maiorIMCNome=i
            if(imc<menorIMC):
                menorIMC=imc
                menorIMCNome=i
                
        #*****************************************
        #   INDICAR A PESSOA COM O MAIOR IMC
        #*****************************************
        print("\nMAIOR IMC :    ",format(maiorIMCNome,"20s"),format(maiorIMC,"10.2f"))
        #*****************************************
        #   INDICAR A PESSOA COM O MENOR IMC
        #*****************************************
        print("MENOR IMC :    ",format(menorIMCNome,"20s"),format(menorIMC,"10.2f"))
        
        
        
        
        