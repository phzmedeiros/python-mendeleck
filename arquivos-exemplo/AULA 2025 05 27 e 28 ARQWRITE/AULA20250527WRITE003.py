# -*- coding: utf-8 -*-
"""
Created on Tue May 27 08:37:43 2025
AULA20250527WRITE003
@author: p226646
"""

dados=[ 
       ["BEETHORYH",10,8],
       ["LYVYA",8,9],
       ["ALLYSSYAH",2,8],
       ["HALLYNNY",2.5,10]
       ]


#ESCREVER OS DADOS DO DATASET
# NO ARQUIVO, COM O SEGUINTE FORMATO:
#     NOME|NOTA1|NOTA2
# ARMAZENAMENTO POR LINHA, INDICANDO
# CADA UM DOS REGISTROS DO DATASET    
arq=open("NOTASEST0103C.TXT","w")
for i in dados:
    nome=i[0]
    nota1=i[1]
    nota2=i[2]
    #ESCREVER NO ARQUIVO
    # ESCREVER SOMENTE STRING
    aux=format(nome,"20s")+"|"+format(nota1,"6.2f")+"|"+format(nota2,"6.2f")
    arq.writelines(aux+"\n")
    
arq.close()    
    
    
    
    