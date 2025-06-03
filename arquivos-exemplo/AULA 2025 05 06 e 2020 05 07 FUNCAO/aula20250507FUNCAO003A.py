# -*- coding: utf-8 -*-
"""
Created on Wed May  7 08:55:40 2025

@author: p226646
"""
vl=[10,9,2,8,10,7,10,9]

#IMPLEMENTAR AS SEGUINTES FUNCOES:
#   1) CALCULAR O MENOR VALOR
#   2) CALCULAR O MAIOR VALOR
#   3) CALCULAR O NUMERO DE ITENS
#   4) CALCULAR A SOMA DOS ITENS

def menor( v ):
    min=v[0]
    for i in v:
        if (i<min):
            min=i   
    return min

def maior( v ):
     max=v[0]
     for i in v:
         if (i>max):
             max=i
     return max

def tamanho( v ):
    tam=0
    for i in v:
        tam=tam+1
    return tam

def soma( v ):
    s=0
    for i in v:
        s=s+i
    return s

#DESENVOLVER UM FUNCAO PARA
# CALCULAR O TAMANHO, MENOR e MAIOR
# VALOR DE UMA LISTA
def tmm( v ):
    tam=tamanho(v)
    min=menor(v)
    max=maior(v)
    return tam,min,max


print("VETOR:   ",vl)
print("MENOR:   ",menor(vl))
print("MAIOR:   ",maior(vl))
print("TAMANHO: ",tamanho(vl))
print("SOMA:    ",soma(vl))

vlTam,vlMin,vlMax=tmm(vl)
print("\nMENOR:   ",vlMin)
print("MAIOR:   ",vlMax)
print("TAMANHO: ",vlTam)

