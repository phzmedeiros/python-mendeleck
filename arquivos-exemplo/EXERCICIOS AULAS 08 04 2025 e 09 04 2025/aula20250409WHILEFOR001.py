# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
pos =0
while(pos<5):
    print(pos)
    pos=pos+1
    
print("\nEXEMPLO COM for")
for pos in range(0,5):
    print(pos)

print("\nEXEMPLO while COM STRING")
nome="GUARANY"
pos=0
tam=len(nome)
while(pos<tam):
    print(pos,"\t",nome[pos])
    pos=pos+1

print("\nEXEMPLO for COM STRING")
nome="GUARANY"
tam=len(nome)
for pos in range(0,tam):
    print(pos,"\t",nome[pos])

print("\nEXEMPLO 2 - for COM STRING")
nome="GUARANY"
tam=len(nome)
for pos in nome:
    print(pos)

print("\nEXEMPLO 3 - for COM STRING")
nome="GUARANY"
tam=len(nome)
for cont,pos in enumerate(nome):
    print(cont,"\t",pos)
    
    