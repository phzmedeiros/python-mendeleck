# -*- coding: utf-8 -*-
"""
Spyder Editor
AULA20250528WRITE006 B
This is a temporary script file.
"""

#DESENVOLVER UMA APLICACAO DE SOFTWARE,
#EM PYTHON, PARA LER OS DADOS DO ARQUIVO
#DADOS:   PRODUTO   QUANTIDADE   PRECOUNITARIO    

arq=open("EMBELEZZA005.TXT","r")
auxArq="  "
while (auxArq!=""):
    auxArq=arq.readline()
    if (auxArq!=""):
        dados=auxArq.split("|")
        produto=dados[0]
        quantidade=dados[1]
        precounitario=dados[2]
        print("PRODUTO:        ",produto)
        print("QUANTIDADE:     ",quantidade)
        print("PRECO UNITARIO: ",precounitario)        

arq.close()
