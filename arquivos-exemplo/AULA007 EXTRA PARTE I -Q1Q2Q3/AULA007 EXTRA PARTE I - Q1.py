# -*- coding: utf-8 -*-
"""
Created on Wed May  7 20:47:30 2025

@author: AM2
"""

#Desenvolver uma função e efetuar a implementação em Python, para separar os dígitos de um número inteiro.

#INVETER A ORDEM DE UM VETOR
def inverter( vl ):
    invertido=[]
    tam=len(vl)
    for i in range(0,tam):
        invertido.append(vl[tam-i-1])
    return invertido


# CONVERTER UM NUMERO INTEIRO EM SEUS DIGITOS
#     vl - NÚMERO INTEIRO
#     RETORNO: digito dos números
def converterDigitos( vl ):
    dg=[]
    
    aux=vl
    while(aux!=0):
          resto=aux%10
          dg.append(resto)
          aux=int(aux/10)
    dg=inverter(dg)
    return dg

vetor=[1,2,3,4,5,6,7,8]
print("\nVETOR:     ",vetor)
print("INVERTIDO: ",inverter(vetor))

numero=1234567
digitos=converterDigitos(numero)
print("\nNUMERO:  ",numero)
print("DIGITOS: ",digitos)