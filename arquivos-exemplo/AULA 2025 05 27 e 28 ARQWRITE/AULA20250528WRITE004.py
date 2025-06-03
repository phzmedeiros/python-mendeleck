# -*- coding: utf-8 -*-
"""
Created on Wed May 28 09:00:42 2025
AULA20250528WRITE004
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

arq=open("ELETRO004.TXT","w")

#LER DOS DADOS:  PRODUTO  QUANTIDADE  PRECO UNITARIO
#  ATRAVES DO TECLADO E GRAVAR NO ARQUIVO
#PARA CADA LEITURA DE DADOS DO TECLADO
#  PERGUNTAR SE DESEJA EFETUAR OUTRO CADASTRO
print("\n\nCADASTRAR DADOS NO ARQUIVO:")
while(True):
    nome=               input("\nNOME DO PRODUTO: ")
    quantidade=   float(input("QUANTIDADE:      "))
    precounitario=float(input("PRECO UNITARIO:  "))
    aux=format(nome,"20s")+"|"+format(quantidade,"6.2f")+"|"+format(precounitario,"10.2f")
    arq.writelines(aux+"\n")
    
    op=input("\nDESEJA OUTRO CADASTRO <S/N> ? ")
    if (op=="N")or(op=="n"):
        break
    
arq.close()