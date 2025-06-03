# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

tam=len(dados)
for pos in range(0,tam):
    print(pos,"\t",dados[pos])

print("\nVERSAO 2")
for registro in dados:
    print(registro)
    
print("\nVERSAO 3")
for registro in dados:
    print("NOME:  ",registro[0])
    print("IDADE: ",registro[1])
    print("SEXO:  ",registro[2]) 
    print("\n")
    
#DESENVOLVER UMA APLICACAO
#PYTHON PARA CONTAR O NUMERO
#DE PESSOAS DO SEXO MASCULINO
#E DO SEXO FEMININO
#MEDIA DE IDADE
#PESSOA COM MAIS IDADE
#E COM MENOR IDADE
somaM=0
somaF=0
maior=-1000000
menor=1000000
soma=0

tam=len(dados)
for registro in dados:
    print(registro)
    #SOMAR PARA CALCULO MEDIA
    soma=soma+registro[1]
    
    #CONTAR MASCULINO
    if (registro[2]=="M"):
        somaM=somaM+1
    #CONTAR FEMININO
    if (registro[2]=="F"):
        somaF=somaF+1        
    
    #MAIOR
    if (registro[1]>maior):
        maior=registro[1]
    #MENOR
    if (registro[1]<menor):
        menor=registro[1]
        
    
media=soma/tam 
print("MEDIA IDADE:  ",format(media,"6.2f"))  
print("MASCULINO:    ",somaM)
print("FEMININO:     ",somaF)
print("MENOR IDADE:  ",menor," ANOS")
print("MAIOR IDADE:  ",maior," ANOS")













    
    
    
    
    
    
    
    
    
    
    