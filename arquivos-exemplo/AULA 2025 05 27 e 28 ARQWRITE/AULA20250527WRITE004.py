# -*- coding: utf-8 -*-
"""
Created on Tue May 27 08:46:05 2025
AULA20250527WRITE004
@author: p226646
"""

dados=[]


arq=open("NOTASEST0103D.TXT","r")
dados=arq.read()
arq.close()

print("DADOS: ",dados)
#SEPARAR OS REGISTROS
# DELIMITADOR \n
reg=dados.split("\n")
print("\nREGISTROS:")
print(reg)


dataset=[]
#SEPARAR OS CAMPOS DE CADA REGISTRO
# DELIMITADOR |
print("\nSEPARANDO OS CAMPOS DOS REGISTROS:")
for i in reg:
    aux=i.split("|")
    print(aux)
    dataset.append(aux)








