# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 10:03:51 2025

@author: p226646
"""

dados=[ 
       ["ADAMASTOR",63,1.75],
       ["LINDOMARIO",71,1.45],
       ["LUKAZ",19,1.72],
       ["JUVENTINA",90,1.45],
       ["ADERBAL",15,1.98],
       ["GUZT AWUZ",30,1.25],
       ["ANNE CLARE",20,1.67],   
       ["BEETHÓRYAH",18,1.86], 
       ["MANNUEUZ",16,1.64],
       ["PERYTHONYO",55,1.56],
       ["MARY LAURE",17,1.81]    
       ]

#LISTAR DADOS DO DATASET
print("\nLISTAGEM REGISTRO DATASET  V1")
tam=len(dados)
for pos in range(0,tam):
    print(pos,"\t",dados[pos])
  
print("\nLISTAGEM REGISTRO DATASET  V2")
tam=len(dados)
for vl in dados:
    print(vl)

print("\nLISTAGEM REGISTRO DATASET  V3")
tam=len(dados)
for pos,vl in enumerate(dados):
    print(pos,"\t",vl)
    
#CADASTRAR/INCLUIR DADOS NO DATASET
nome="MANU ELLAH"
idade=16
altura=1.78
aux=[nome,idade,altura]
dados.append(aux)

print("\nLISTAGEM REGISTRO DATASET  V4")
tam=len(dados)
for pos,vl in enumerate(dados):
    print(pos,"\t",vl)
    
#EFETUAR A LEITURA DO NOME, IDADE e ALTURA
#DE UM(a) AMIGO(a) E CADASTRAR EM dados
#LISTAR dados APOS O CADASTRO
nomeamigo=input("DIGITAR NOME:  ")
idadeamigo=int(input("DIGITAR IDADE: "))
alturaamigo=float(input("DIGITAR ALTURA: "))
lista=[nomeamigo,idadeamigo,alturaamigo]
dados.append(lista )

print("\nLISTAGEM REGISTRO DATASET  V5")
tam=len(dados)
for pos,vl in enumerate(dados):
    print(pos,"\t",vl)

#EFETUAR A LEITURA DO NOME, IDADE e ALTURA
#DE n AMIGOS(as) E CADASTRAR EM dados
#LISTAR dados APOS TODOS OS CADASTROS
while(True):
    nomeamigo=input("DIGITAR NOME:  ")
    idadeamigo=int(input("DIGITAR IDADE: "))
    alturaamigo=float(input("DIGITAR ALTURA: "))
    lista=[nomeamigo,idadeamigo,alturaamigo]
    dados.append(lista )  
    opcao=input("DESEJA OUTRO CADASTRO <S/N> ")
    if (opcao=="N") or (opcao=="n"):
        break
print("\nLISTAGEM REGISTRO DATASET  V6")
tam=len(dados)
for pos,vl in enumerate(dados):
    print(pos,"\t",vl)





