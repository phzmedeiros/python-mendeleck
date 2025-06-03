# -*- coding: utf-8 -*-
"""
Created on Wed May  7 10:41:39 2025
aula20250507FUNCAO003B
@author: p226646
"""
vl=[10,9,2,8,10,7,10,9]

#IMPLEMENTAR AS SEGUINTES FUNCOES:
#   1) CALCULAR O MENOR VALOR
#   2) CALCULAR O MAIOR VALOR
#   3) CALCULAR O NUMERO DE ITENS
#   4) CALCULAR A SOMA DOS ITENS

def minimo( v ):
    menor=v[0]
    for i in v:
        if (i<menor):
            menor = i
    return menor

def maximo( v ):
    maior=v[0]
    for i in v:
        if (i>maior):
            maior=i
    return maior

def tamanho( v ):
    tam=0
    for i in v:
        tam=tam+1
    return tam

def somar( v ):
    soma=0
    for i in v:
        soma=soma+i 
    return  soma

#DESENVOLVER UMA FUNCAO PARA
#RETORNAR O NUMERO DE ELEMENTOS DE UMA LISTA,
#  O MENOR E O MAIOR VALOR
def tmm( v ):
    tam=tamanho(v)
    menor=minimo(v)
    maior=maximo(v)
    return tam,menor,maior

print("\nVETOR:  ",vl)
print("MENOR VALOR:   ",minimo(vl))
print("MAIOR VALOR:   ",maximo(vl))
print("TAMANHO:       ",tamanho(vl))
print("TOTAL VALORES: ",somar(vl))

nItens,vlMenor,vlMaior=tmm(vl)
print("\nTAMANHO:       ",nItens)
print("MENOR VALOR:   ",vlMenor)
print("MAIOR VALOR:   ",vlMaior)


resultado=tmm(vl)
print("\nRESULTADO: ",resultado)
print("TAMANHO:       ",resultado[0])
print("MENOR VALOR:   ",resultado[1])
print("MAIOR VALOR:   ",resultado[2])

