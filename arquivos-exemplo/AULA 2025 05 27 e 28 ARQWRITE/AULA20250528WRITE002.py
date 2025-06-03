# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:43:07 2025
AULA20250528WRITE002
@author: p226646
"""

dataset=[
          ["REFRIGERADOR REFREE",10,1234.56],
          ["XAPYNHA",25,179.99],
          ["SSANDUYXEYRA",40,99.99],
          ["MYKRO HONDA",15,520.99]
         ]

#LISTAR OS DADOS NO CONSOLE
for i in dataset:
    print(i)
    print("NOME:              ",i[0])
    print("QUANTIDADE:        ",i[1])
    print("PRECO UNITARIO:  R$",i[2])

arq=open("ELETRO002.TXT","w")
for i in dataset:
    nome=i[0]
    quantidade=i[1]
    precounitario=i[2]
    aux=nome+"|"+str(quantidade)+"|"+str(precounitario)
    arq.writelines(aux+"\n")
    
arq.close()