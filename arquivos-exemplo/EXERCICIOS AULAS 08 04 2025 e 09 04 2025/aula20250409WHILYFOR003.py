# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 09:07:36 2025

@author: p226646
"""

#DADO O DATASET A SEGUIR,
#CALCULAR O VALOR MEDIO, MAIOR e MENOR
#UTILIZAR OBRIGATORIAMENTE  for 
#         SEM CONTADOR

idade=[15, 18, 17, 42, 98, 104, 17]
soma=0
maior=-100000
menor=10000
for valor in idade:
    print(valor)
    soma=soma+valor
    if (valor>maior):
        maior=valor
    if (valor<menor):
        menor=valor
        
media=soma/len(idade)
print("MEDIA: ",format(media,"6.2f"))
print("MENOR: ",format(menor,"6.2f"))
print("MAIOR: ",format(maior,"6.2f"))





