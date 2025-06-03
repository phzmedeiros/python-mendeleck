# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import random

palavras=["GUARANY","CAMPEAO","ANDRE","CAMPINAS"]
nPalavras=len(palavras)
posPL=random.randint(0,nPalavras-1)
pl=palavras[posPL]
nLetras=len(pl)

cont=0
showpl=[]
pl=[]

while (cont<nLetras):
    showpl.append("*")
    pl.append(palavras[posPL][cont])
    cont=cont+1
    
flagAcertou=0
tentativas=0

while(flagAcertou!=1):
    tentativas=tentativas+1
    #MOSTRAR O ESPACO DAS LETRAS
    print("PALAVRA: ",showpl)
    
    #LER UMA LETRA
    l=input("DIGITE UMA LETRA: ")
    
    #PESQUISAR OCORRENCIA DA LETRA
    cont=0
    while(cont<nLetras):
        if(pl[cont]==l):
            showpl[cont]=l
        cont=cont+1    
    
    #VERIFICAR SE ACERTOU
    if ("*" not in showpl):
        flagAcertou=1
        
print("PARABENS, VOCE ACERTOU A PALAVRA: ",palavras[posPL], " EM ",tentativas," TENTATIVAS" )


