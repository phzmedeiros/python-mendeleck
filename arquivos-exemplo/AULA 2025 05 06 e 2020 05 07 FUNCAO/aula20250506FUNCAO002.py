# -*- coding: utf-8 -*-
"""
Created on Tue May  6 08:24:31 2025

@author: P226646
"""

#DESENVOLVER UMA FUNCAO PARA
#CALCULAR A MEDIA DE UMA LISTA
#DE VALORES

vl=[3,8,2.5,6,10,9]

def media(notas):
    tam=len(notas)
    soma=0
    for i in notas:
        soma=soma+i
    md=soma/tam
    return md

valorMedia=media(vl)
print("MEDIA= ",valorMedia)






