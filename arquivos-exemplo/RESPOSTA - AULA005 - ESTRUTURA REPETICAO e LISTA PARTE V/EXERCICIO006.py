# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 21:55:39 2025

@author: AM2
"""

# A software house Ç3Pó-2S2, 
# tem outra demanda para você. 
# Desenvolva uma aplicação de software 
# para ler uma frase, através do teclado,
# e separar todas as palavras formando 
# uma lista de palavras.
# EXEMPLO:
# Frase=“PANTURRYLHA VIAJOU PARA RAPIDÓPOLIS”
#
# PALAVRAS=[“PANTURRYLHA” , “VIAJOU”, “PARA” , “RAPIDÓPOLIS”]

frase=input("DIGITE A FRASE - USAR LETRA MAIUSCULA: ")
#frase="PANTURRYLHA VIAJOU PARA RAPIDÓPOLIS"

tam = len(frase)

#PALAVRAS
pl=[]

auxpl=""

#SEPARAR PALAVRAS
# ESPACO EM BRANCO UTILIZADO
# PARA IDENTIFICAR PALAVRA
pos=0
while(pos<tam):
    if (frase[pos]!=" "):
        auxpl=auxpl+frase[pos]
    else:
        print(auxpl)
        pl.append(auxpl)
        auxpl=""
    pos=pos+1

#SEPARA ULTIMA PALAVRA DA FRASE    
print(auxpl)
pl.append(auxpl)   


tampl=len(pl)
print("\nFRASE: ",frase)
print("NUMERO DE PALAVRAS IDENTIFICADAS: ",tampl)
print("PALAVRAS IDENTIFICADAS:")
pos=0
while(pos<tampl):
   print(pos,"\t",pl[pos])
   pos=pos+1
        



