# -*- coding: utf-8 -*-
"""
Spyder Editor
AULA20250528WRITE004 B
This is a temporary script file.
"""

dataset=[
           ["XAMPOO KYABU",10,123.67],
           ["KLYER MAN",25,210.99],
           ["GEKYTYZ",12,99.99],
           ["YZMAUTY",48,1000.99],
           ["MAU BEK",15,249.99]
         ]

#LISTAR OS DADOS DO DATASET
for i in dataset:
    print("\n",i)
    produto=i[0]
    quantidade=i[1]
    precounitario=i[2]
    print("PRODUTO:        ",produto)
    print("QUANTIDADE:     ",quantidade)
    print("PRECO UNITARIO: ",precounitario)
    
#GRAVAR OS DADOS NO ARQUIVO
arq=open("EMBELEZZA004.TXT","w")
for i in dataset:
    produto=i[0]
    quantidade=i[1]
    precounitario=i[2]
    aux=format(produto,"20s")+"|"+format(quantidade,"6.2f")+"|"+format(precounitario,"10.2f")                                       
    arq.writelines(aux+"\n")
 
arq.close()
