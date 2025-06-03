# -*- coding: utf-8 -*-
"""
Spyder Editor
AULA20250528WRITE001
This is a temporary script file.
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

arq=open("ELETRO001.TXT","w")
for i in dataset:
    nome=i[0]
    quantidade=i[1]
    precounitario=i[2]
    arq.writelines(nome+"\n")
    arq.writelines(str(quantidade)+"\n")
    arq.writelines(str(precounitario)+"\n")
    
arq.close()





