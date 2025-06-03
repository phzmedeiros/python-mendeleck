# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("\nPRIMEIRA OPACAO DE LEITURA")
arquivo=open("ARQ20250520-001.txt","r")

#LER O ARQUIVO INTEIRO
aux0=arquivo.read()
print(aux0)
arquivo.close()


print("\nSEGUNDA OPCAO DE LEITURA")
arquivo=open("ARQ20250520-001.txt","r")

aux=" "
while(aux!=""):
    aux=arquivo.readline()
    aux1=aux.split("\n")
    print(aux1[0])
    
arquivo.close()










