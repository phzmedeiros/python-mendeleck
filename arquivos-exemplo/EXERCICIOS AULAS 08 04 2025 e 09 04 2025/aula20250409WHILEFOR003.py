# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:33:18 2025

@author: p226646
"""

#LISTAR OS CARACTERES DA SEGUINTE FRASE
#***** UTILIZAR OBRIGATORIAMENTE for

frase="GUARANY GRANDE CAMPEAO BRASILEIRO DE 1978."

tam=len(frase)
for pos in range(0,tam):
    print(pos,"\t",frase[pos])
    
print("\nSOLUCAO 2:")   
for  pos in frase:
    print(pos)

#UTILIZANDO O CODIGO ANTERIOR
#CONTAR O NUMERO DE CARACTERES EM BRANCO
#UTILIZAR OBRIGATORIAMENTE for
print("\nCONTAR ESPACOS EM BRANCOS")
somaBranco=0
for pos in range(0,tam):
    print(pos,"\t",frase[pos])
    if (frase[pos]==" "):
        somaBranco=somaBranco+1

print("NUMERO DE ESPACOS EM BRANCO: ",somaBranco)

print("\nCONTAR ESPACOS EM BRANCOS - VERSAO 2")
somaBranco=0
for pos in frase:
    print(pos)
    if (pos==" "):
        somaBranco=somaBranco+1

print("NUMERO DE ESPACOS EM BRANCO: ",somaBranco)

print("\nCONTAR ESPACOS EM BRANCOS - VERSAO 3")
somaBranco=0
for contInterno, pos in enumerate(frase):
    print(contInterno,"\t",pos)
    if (pos==" "):
        somaBranco=somaBranco+1

print("NUMERO DE ESPACOS EM BRANCO: ",somaBranco)


#UTILIZANDO OS CODIGOS ANTERIORES
#CONTAR O NUMERO DE VOGAIS
#CONTAR O NUMERO DE LETRAS "A"
#CONTAR O NUMERO DE LETRAS "E"
#CONTAR O NUMERO DE LETRAS "I"
#CONTAR O NUMERO DE LETRAS "O"
#CONTAR O NUMERO DE LETRAS "U"
#UTILIZAR OBRIGATORIAMENTE for
print("\n\nCONTAR VOGAIS - SOLUCAO 1")
contVogal=0
contA=0
contE=0
contI=0
contO=0
contU=0
for letra in frase:
    if (letra=="A")or(letra=="E")or(letra=="I")or (letra=="O")or(letra=="U"):
             contVogal=contVogal+1
    if (letra=="A"):
          contA=contA+1         
    if (letra=="E"):
          contE=contE+1  
    if (letra=="I"):
          contI=contI+1  
    if (letra=="O"):
          contO=contO+1  
    if (letra=="U"):
          contU=contU+1  

print("\nNUMERO DE VOGAIS: ",contVogal)
print("NUMERO VOGAL [A]: ",contA)
print("NUMERO VOGAL [E]: ",contE)
print("NUMERO VOGAL [I]: ",contI)
print("NUMERO VOGAL [O]: ",contO)
print("NUMERO VOGAL [U]: ",contU)


print("\n\nCONTAR VOGAIS - SOLUCAO 2")
contVogal=0
contA=0
contE=0
contI=0
contO=0
contU=0
for letra in frase:
    if (letra=="A"):
          contA=contA+1         
    elif (letra=="E"):
          contE=contE+1  
    elif (letra=="I"):
          contI=contI+1  
    elif (letra=="O"):
          contO=contO+1  
    elif (letra=="U"):
          contU=contU+1  

contVogal=contA+contE+contI+contO+contU
print("\nNUMERO DE VOGAIS: ",contVogal)
print("NUMERO VOGAL [A]: ",contA)
print("NUMERO VOGAL [E]: ",contE)
print("NUMERO VOGAL [I]: ",contI)
print("NUMERO VOGAL [O]: ",contO)
print("NUMERO VOGAL [U]: ",contU)