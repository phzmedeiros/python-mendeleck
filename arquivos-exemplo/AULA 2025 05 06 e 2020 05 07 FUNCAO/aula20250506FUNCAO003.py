# -*- coding: utf-8 -*-
"""
Created on Tue May  6 08:41:15 2025

@author: P226646
"""

#DESENVOLVER UM CONJUNTO DE FUNCOES
#PARA CALCULAR O VALOR MAXIMO,
# VALOR MINIMO e A SOMA DE VALORES
# DE UMA LISTA

def maximo(vl):
    max=vl[0]
    for i in vl:
        if i>max:
            max=i
    return max

def minimo(vl):
    min=vl[0]
    for i in vl:
        if i<min:
            min=i
    return min

def total(vl):
    soma=0
    for i in vl:
        soma=soma+i
    return soma

#CALCULAR P NUMERO DE VALORES DE UMA LISTA
def tamanho(vl):
    soma=0
    for i in vl:
        soma=soma+1
    
    return soma

#DEFINIR UMA FUNCAO PARA RETORNAR:
# NUMERO DE ITENS DE UMA LISTA
# VALOR MINIMO
# VALOR MAXIMO
def tamMinMax(vl):
    tam=tamanho(vl)
    min=minimo(vl)
    max=maximo(vl)
    return tam,min,max


valores=[10,9,10,2,1.5,9]
print("VALOR MINIMO: ",minimo(valores))
print("VALOR MAXIMO: ",maximo(valores))
print("TOTAL DOS VALORES: ",total(valores))

print("TAMANHO valores: ",tamanho(valores))

frase="JUVENAL FOI ATE RAPIDOPOLIS"
print("TANHANHO DA FRASE: ",tamanho(frase))


tam,min,max=tamMinMax(valores)
print(tam,"\t",min,"\t",max)









 