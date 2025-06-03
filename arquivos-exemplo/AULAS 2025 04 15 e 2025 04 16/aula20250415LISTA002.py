# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 09:12:38 2025

@author: p226646
"""

dados=[
        ["JUVENTINA",90,"F"],
        ["LYVYAURA",39,"F"],
        ["ADERBAL",15,"M"],
        ["BYTHOR",30,"M"],
        ["PYTHER",20,"M"],
        ["BEETHÓRYAH",18,"F"],
        ["MANNUEU",16,"M"],
        ["PERYTHONYO",55,"M"]
       ]

nome="GERTRUDYZ"
idade=100
sexo="F"

cadastro=[nome,idade,sexo]
dados.append(cadastro)

#DESENVOLVER UMA APLICACAO
#PARA LER OS DADOS [nome,idade,sexo]
#DE 5 PESSOAS, CADASTRAR (ACRESCENTAR)
#NO DATASET dados E LISTAR TODOS OS
#REGISTROS
pos=0
while (pos<2):
    print("\nCADASTRO: ",pos)
    nome=input( "DIGITE O NOME:  ")
    idade=input("DIGITE A IDADE: ")
    sexo=input( "DIGITE O SEXO:  ")
    
    #ESTRUTURANDO O REGISTRO
    registro=[nome,idade,sexo]
    #ACRESCENTANDO O REGISTRO NO DATASET
    dados.append(registro)
    
    pos = pos+1
    
for registro in dados:
    print(registro)
    
print("DADOS CADASTRADOS")
for registro in dados:
    #SEPARANDO OS CAMPOS DO REGISTRO
    nome,idade,sexo=registro
    print("NOME:   ",nome)
    print("IDADE:  ",idade)
    print("SEXO:   ",sexo)
    print("\n")










