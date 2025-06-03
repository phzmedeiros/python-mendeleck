# -*- coding: utf-8 -*-
"""
Created on Wed May  7 08:32:12 2025

@author: p226646
"""

#IMPLEMENTAR A SEGUINTE FUNCAO:
#   CALCULAR A MEDIA DE UMA LISTA 
#   DE VALORES

vl=[10,9,2,8,10,7,10,9]

def media( gustavo ):
    soma=0
    for i in gustavo:
        soma=soma+i
    md=soma/len(gustavo)
    return md

print("\nMEDIA: ",media(vl))



