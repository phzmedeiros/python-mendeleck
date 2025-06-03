# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:15:24 2025

@author: p226646
"""

nome="GUARANY"
tam=len(nome)
pos=0
while(pos<tam):
    print(pos,"\t",nome[pos])
    pos=pos+1

print("\nIMPLEMENTACAO COM for")
for pos in range(0,tam):
    print(pos,"\t",nome[pos])

print("\nIMPLEMENTACAO COM for INDIRETO")
for pos in nome:
    print(pos)

print("\nIMPLEMENTACAO COM for INDIRETO")
print("   COM CONTAGEM")
for contInterno, pos in enumerate(nome):
    print(contInterno,"\t",pos)
    




