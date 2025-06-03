# -*- coding: utf-8 -*-
"""
Created on Wed May  7 21:15:27 2025

@author: AM2
"""

#Desenvolver uma função e efetuar a implementação em Python, 
#para converter um número binário em decimal.
def converterBinarioDecimal( vlbim ):
    aux=str(vlbim)
    tam=len(aux)
    soma=0
    for i in range(0,tam):
        soma=soma+int(aux[tam-i-1])*2**i
    return soma
    


valorbinario=11011
decimal=converterBinarioDecimal(valorbinario)
print("\nVALOR BINARIO:  ",valorbinario)
print("VALOR DECIMAL:  ",decimal)


valorbinario=110111101
decimal=converterBinarioDecimal(valorbinario)
print("\nVALOR BINARIO:  ",valorbinario)
print("VALOR DECIMAL:  ",decimal)
