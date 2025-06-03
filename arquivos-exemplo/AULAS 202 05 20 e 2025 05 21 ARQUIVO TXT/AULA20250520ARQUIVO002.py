# -*- coding: utf-8 -*-
"""
Created on Tue May 20 08:39:37 2025

@author: p226646
"""

#LER O ARQUIVO: ARQ20250520-002.TXT
#APRESENTAR OS VALORES NO CONSOLE
# E CALCULAR A MEDIA

print("\nLEITURA DOS DADOS")
arquivo=open("ARQ20250520-002.txt","r")
soma=0
aux=" "
cont=0
while(aux!=""):
    aux=arquivo.readline()
    aux1=aux.split("\n")
    if(aux!=""):
        print(aux1[0])
        soma=soma+int(aux1[0])
        cont=cont+1
 
media=soma/cont
print("MEDIA: ",format(media,"6.2f"))
arquivo.close()