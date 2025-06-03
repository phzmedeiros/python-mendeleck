# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 21:07:07 2025

@author: AM2
"""

# A empresa GELO – Global Electronic Limited Operation 
# está desenvolvendo um sensor de temperatura para 
# aplicações automobilísticas.
# Durante um dos testes, coletou-se valores de 
# temperatura em graus celsius.

# Utilizando os dados apresentados na lista, 
# desenvolva uma aplicação de software, 
# utilizando a linguagem Python, para calcular:

# 1) O valor médio de temperatura
# 2) O valor mínimo de temperatura
# 3) O valor máximo de temperatura


# LISTA DE TEMPERATURAS
Temperatura=[10,12,9,8,9,9,10,11,12,14,12,11]  

tam = len(Temperatura)

soma=0
maior=-1000000
menor=100000

pos=0
while (pos < tam):
    print("POS: ",pos,"\t TEMPERATURA: ",Temperatura[pos])
    soma=soma+Temperatura[pos]
    if (Temperatura[pos]>maior):
        maior=Temperatura[pos]
    if (Temperatura[pos]<menor):
        menor=Temperatura[pos]   
    pos=pos+1
        
media=soma/tam
print("TEMPERATURA MEDIA: ",format(media,"6.2f"))
print("MENOR TEMPERATURA: ",format(menor,"6.2f"))   
print("MAIOR TEMPERATURA: ",format(maior,"6.2f"))


     
        