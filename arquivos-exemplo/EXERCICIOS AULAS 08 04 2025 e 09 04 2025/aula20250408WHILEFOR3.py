# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 08:36:39 2025

@author: p226646
"""

#DESENVOLVER UMA APLICACAO DE
#SOFTWARE PARA LER UMA PALAVRA
#E IMPRIMIR AS LETRAS - USAR FOR

pl=input("DIGITE PALAVRA: ")

print("\nVERSAO 1:")
#pos NESTE CASO ESTA ASSOCIADO
#  AS LETRAS DA PALAVRA pl
for pos in pl:
    print(pos)

print("\nVERSAO 2:")
tam=len(pl)
#pos NESTE CASO Eh UM CONTADOR
print("POS  LETRAS")
for pos in range(0,tam):
    print(pos,"\t",pl[pos])
    
    
    



