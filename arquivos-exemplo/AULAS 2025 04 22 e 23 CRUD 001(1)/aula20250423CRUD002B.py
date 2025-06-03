# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:29:34 2025

@author: p226646
"""

#*********************************
#CADASTRAR
#*********************************
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


nome=input("DIGITE O NOME:   ")
idade=int(input("DIGITE A IDADE:  "))
altura=float(input("DIGITE ALTURA:   "))

aux=[nome,idade,altura]

dados.append(aux)


for vl in dados:
    print(vl)





