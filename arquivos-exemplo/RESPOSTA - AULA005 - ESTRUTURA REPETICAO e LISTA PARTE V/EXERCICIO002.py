# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 21:14:16 2025

@author: AM2
"""

# A Dra. Panturrilha está realizando uma série de experimentos 
# com medicamentos para o tratamento de celulite. 
# Na atual fase de testes, os pacientes recebem uma dose do 
# fármaco e durante 10 dias, utilizando uma fita reagente, 
# monitoram o ph da pele e anotam o valor em uma planilha 
# como mostrado da lista apresentada a seguir.
# Utilizando os dados apresentados, desenvolva uma aplicação 
# de software, utilizando a linguagem Python, para calcular:

#    1) O valor médio do ph
#   2) O valor mínimo e máximo
#   3) Contar o número de valores que são menores e maiores que o valor médio

ph=[7 ,6 ,7.5 ,7 ,6.8 ,7.1 ,6.9 ,6.4 ,6.5 ,6.7]  

tam = len(ph)

soma=0
maior=-1000000
menor=100000

pos=0
while (pos < tam):
    print("POS: ",pos,"\t PH: ",ph[pos])
    soma=soma+ph[pos]
    if (ph[pos]>maior):
        maior=ph[pos]
    if (ph[pos]<menor):
        menor=ph[pos]   
    pos=pos+1
        
media=soma/tam
print("PH MEDIO: ",format(media,"6.2f"))
print("MENOR PH: ",format(menor,"6.2f"))   
print("MAIOR PH: ",format(maior,"6.2f"))

# CALCULAR O NUMERO DE VALORES MAIORES E MENORES QUE A MEDIA
maiorMedia=0
menorMedia=0

pos=0
while (pos < tam):
    if (ph[pos]>=media):
        maiorMedia=maiorMedia+1
    if (ph[pos]<media):
        menorMedia=menorMedia+1
    pos=pos+1
    
print("NUMERO DE PH MENORES QUE A MEDIA   : ",format(menorMedia,"4d"))   
print("NUMERO DE PH MAIO IGUAL QUE A MEDIA: ",format(maiorMedia,"4d"))   
