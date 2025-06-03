# -*- coding: utf-8 -*-
"""
Created on Wed May  7 10:21:44 2025
aula20250507FUNCAO002B
@author: p226646
"""

#IMPLEMENTAR A SEGUINTE FUNCAO:
#   CALCULAR A MEDIA DE UMA LISTA 
#   DE VALORES

#ATENCAO: AS VARIAVEIS v , soma , i E md
#         SÃO VARIAVEIS LOCAIS
#         SÃO VARIAVEIS INTERNAS DA FUNCAO
#         OU SEJA, NAO PODEM SER ACESSADAS
#         EXTERNAMENTE
#         ASSIM, POSSO ESCOLHER QUALQUER 
#         NOME PARA AS VARIAVEIS
def media( v ):
    soma=0
    for i in v:
        soma=soma+i
    md=soma/len(v)
    return md

vl=[10,9,2,8,10,7,10,9]

vlm=media(vl)
print("MEDIA: ",vlm)

