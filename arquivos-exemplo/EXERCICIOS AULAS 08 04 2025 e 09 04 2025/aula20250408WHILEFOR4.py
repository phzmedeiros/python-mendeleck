# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 08:53:07 2025

@author: p226646
"""

#DESENVOLVER UMA APLICACAO DE 
#SOFTWARE PARA LER UMA SEQUENCIA DE
#CARACTERES NUMERICOS e SOMAR OS
#VALORES DE CADAS CARACTER
#EXEMPLO:   pl="5826"
#          soma = 5+8+2+6 = 21
#
#IMPLEMENTAR UTILIZANDO for

pl=input("DIGITAR NUMERO: ")
soma=0
for pos in pl:
    print(pos)
    soma=soma+int(pos)

print("TOTAL= ",soma)

print("\nSOLUCAO 2:")
soma=0
tam=len(pl)
#OBSERVE QUE pos Eh UM CONTADOR
for pos in range(0,tam):
    print(pos,"\t",pl[pos])
    soma=soma+int(pl[pos])

print("TOTAL= ",soma)




