# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 21:50:16 2025

@author: AM2
"""

# A software house Ç3Pó-2S2, 
# gestora do dicionário horélyuMM, 
# deseja verificar a existência de 
# um possível email em uma frase. 
# Você foi convocado a desenvolver 
# uma aplicação de software para ler 
# uma frase, através do teclado,
# e verificar a existência do 
# caracter “@” no texto.

frase=input("DIGITE A FRASE: ")

#frase="andre.mendeleck@gmail.com"

tam = len(frase)

chaveEmail=0

pos=0
while(pos<tam):
    #VERIFICAR @
    if (frase[pos]=="@"):
        chaveEmail=1

    pos=pos+1

print("\nFRASE: ",frase)

if (chaveEmail==1):
   print("\nA FRASE PODE CONTER UM EMAIL")
else:
   print("\nPROVAVELMENTE A FRASE NAO CONTEM EMAIL")






