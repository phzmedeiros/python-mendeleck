# -*- coding: utf-8 -*-
"""
Created on Tue May 20 08:55:56 2025

@author: p226646
"""
#LER O ARQUIVO: ARQ20250520-003.TXT
#CONTENDO: NOME e IDADE
#APRESENTAR OS VALORES NO CONSOLE
# E CALCULAR A MEDIA DE IDADE

print("\nLEITURA DOS DADOS")
arquivo=open("ARQ20250520-003.txt","r")

somaIdade=0
cont=0

auxNome=" "
auxIdade=" "
while(auxNome!=""):
    auxNome=arquivo.readline()
    aux=auxNome.split("\n")
    nome=aux[0]
    
    auxIdade=arquivo.readline()
    aux=auxIdade.split("\n")
    if(auxNome!=""):
        idade=int(aux[0])
        somaIdade=somaIdade+idade
        cont=cont+1
        print(nome,"\t",idade)
 
media=somaIdade/cont
print("MEDIA:  ",format(media,"6.2f"))
arquivo.close()





