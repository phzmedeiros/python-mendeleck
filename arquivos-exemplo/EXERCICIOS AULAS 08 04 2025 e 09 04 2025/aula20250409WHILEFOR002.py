# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 08:36:21 2025

@author: p226646
"""

#LISTAR OS CARACTERES DA SEGUINTE FRASE
#***** UTILIZAR OBRIGATORIAMENTE for

frase="GUARANY CAMPEAO BRASILEIRO DE 1978."
for letra in frase:
    print(letra )


#UTILIZANDO O CODIGO ANTERIOR
#CONTAR O NUMERO DE ESPACOS EM BRANCO
#***** UTILIZAR OBRIGATORIAMENTE for
tam=len(frase)
contarBranco=0
for pos in range(0,tam):
     print(pos,"\t",frase[pos])
     if (frase[pos]==" "):
         contarBranco=contarBranco+1
print("NUMERO DE ESPACOS EM BRANCOS: ",contarBranco)

print("\nVERSAO 2")
tam=len(frase)
contarBranco=0
for letra in frase:
    print(letra)
    if (letra==" "):
        contarBranco=contarBranco+1
print("NUMERO DE ESPACOS EM BRANCOS: ",contarBranco)
   
print("\nVERSAO 3 - COM enumerate")
tam=len(frase)
contarBranco=0
for cont,letra in enumerate(frase):
    print(cont,"\t",letra)
    if (letra==" "):
        contarBranco=contarBranco+1
print("NUMERO DE ESPACOS EM BRANCOS: ",contarBranco)
      
    
    
    




