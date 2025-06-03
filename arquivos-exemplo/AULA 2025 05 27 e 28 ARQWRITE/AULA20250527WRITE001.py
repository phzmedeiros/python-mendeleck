# -*- coding: utf-8 -*-
"""
Created on Tue May 27 08:08:52 2025
AULA20250527WRITE001
@author: p226646
"""
dados=[ 
       ["BEETHORYH",10,8],
       ["LYVYA",8,9],
       ["ALLYSSYAH",2,8],
       ["HALLYNNY",2.5,10]
       ]


#LISTAR OS DADOS
for i in dados:
    print(i)
    nome=i[0]
    nota1=i[1]
    nota2=i[2]
    print(nome,"\t",nota1,"\t",nota2)
    
arq=open("NOTASEST0103.TXT","w")
for i in dados:
    nome=i[0]
    nota1=i[1]
    nota2=i[2]
    #ESCREVER NO ARQUIVO
    # ESCREVER SOMENTE STRING
    arq.writelines(nome+"\n")
    arq.writelines(str(nota1)+"\n")
    arq.writelines(str(nota2)+"\n")
    
arq.close()





