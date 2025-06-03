# -*- coding: utf-8 -*-
"""
Created on Sun May 18 11:32:43 2025

@author: AM2
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import math

import pandas as pd
from pandas import read_csv
from pandas import set_option

#*******************************************
#  CRIANDO O PONTEIRO PARA UM ARQUIVO
#*******************************************
# 'r': modo de leitura, o arquivo deve existir previamente
# 'w': modo de escrita, se o arquivo não existir, ele será criado
# 'a': modo de anexar, adiciona informações ao final do arquivo
# 'x': modo exclusivo, cria um novo arquivo somente se ele não existir
# 'b': modo binário, usado para arquivos binários, como imagens ou vídeos
# 't': modo de texto, usado para arquivos de texto
arquivo = open('EXEMPLOTXTCRUD001.txt', 'r')


# LEITURA DOS DADOS DO ARQUIVO 
# INFORMACOES POR CARACTER
# LEITURA DO ARQUIVO COMPLETO
conteudo = arquivo.read()

#IMPRIMIR O CONTEUDO LIDO DIRETAMENTE
# DO ARQUIVO, SEM TRATAMENTO
#NO CONSOLE, DIGITE:  conteudo
# OBSERVE QUEO RESULTADO SERA:  '01234\n56789\n'
#OS DADOS, NO ARQUIVO, SÃO SEQUENCIAIS, INCLUINDO O \n
print("\nCONTEUDO LIDO DO ARQUIVO: ",conteudo)

input("DIGITE ALGO PARA CONTINUAR 1:  ")


# IMPRIMIR POR CARACTER
print("\nIMPRIMIR CARACTERES:")
for i in conteudo:
    print(i)

input("DIGITE ALGO PARA CONTINUAR 2:  ")

# SEPARAR AS LINHAS NA VARIÁVEL CONTEUDO
# UTILIAR SEGMENTAÇÃO - split
# RECORTAR POR LINHA
x=conteudo.split("\n")

# IMPRIMIR POR LINHA
print("\nIMPRIMIR POR LINHA")
for i in x:
    print(i)

#FECHAR O ARQUIVO    
arquivo.close()   
    
input("DIGITE ALGO PARA CONTINUAR 3:  ")

#******************************************
# OUTRA ABORDAGEM PARA ABERTURA DO ARQUIVO
#******************************************
arquivo = open('EXEMPLOTXTCRUD001.txt', 'r')
print("\n\nOUTRA ABORDAGEM PARA A LEITURA DOS DADOS DO ARQUIVO")
conteudo=" "
while (conteudo!=""):
    conteudo = arquivo.read(1)
    print(conteudo,end="")
    
arquivo.close()

input("DIGITE ALGO PARA CONTINUAR 4:  ")

#************************************************************
#  CRIANDO O PONTEIRO PARA UM ARQUIVO - ESCREVER NO ARQUIVO
#************************************************************
# 'w': modo de escrita, se o arquivo não existir, ele será criado
arquivo = open('EXEMPLOTXTCRUD001b.txt', 'w')

nome="NYOBYO"
idade="89"
altura="1.78"

arquivo.writelines(nome+"\n")
arquivo.writelines(idade+"\n")
arquivo.writelines(altura+"\n")

arquivo.close()

#LENDO OS DADOS GRAVADOS
arquivo = open('EXEMPLOTXTCRUD001b.txt', 'r')

# LEITURA DOS DADOS DO ARQUIVO 
# INFORMACOES POR CARACTER
# LEITURA DO ARQUIVO COMPLETO
conteudo = arquivo.read()

#IMPRIMIR O CONTEUDO LIDO DIRETAMENTE
# DO ARQUIVO, SEM TRATAMENTO
#NO CONSOLE, DIGITE:  conteudo
# OBSERVE QUEO RESULTADO SERA:  
# 'JUVENAL E PERCIVAL SAO AMIGOS\nJUVENAL ESTUDA NA PUC-CAMPINAS\nPERCIVAL ESTUDA NA PUC-RAPIDOPOLIS\nFIM\n'
#OS DADOS, NO ARQUIVO, SÃO SEQUENCIAIS, INCLUINDO O \n
print("\nCONTEUDO LIDO DO ARQUIVO: \n")
print(conteudo)


# SEPARAR AS LINHAS NA VARIÁVEL CONTEUDO
# UTILIAR SEGMENTAÇÃO - split
# RECORTAR POR LINHA
linhas=conteudo.split("\n")

print("\nIMPRIMIR AS LINHAS: ")
print(linhas)

# IMPRIMIR POR LINHA
print("\n\nIMPRIMIR POR LINHA:\n")
for i in linhas:
    print(i)

# IMPRIMIR POR LINHA
print("\n\nIMPRIMIR POR LINHA:\n")
print("TAM\tCONTEUDO")
for i in linhas:
    print(len(i),"\t",i)


#FECHAR O ARQUIVO    
arquivo.close() 

input("DIGITE ALGO PARA CONTINUAR 5:  ")


#****************************************************************
# OUTRA ABORDAGEM PARA ABERTURA DO ARQUIVO - MONTANDO O DATASET
#****************************************************************
arquivo = open('EXEMPLOTXTCRUD001.txt', 'r')
print("\n\nOUTRA ABORDAGEM PARA A")
print("LEITURA DOS DADOS DO ARQUIVO")
print("LEITURA POR LINHA:\n")
#LENDO OS DADOS GRAVADOS
arquivo = open('EXEMPLOTXTCRUD001.txt', 'r')    
flagFImArquivo=" "
dados=[]
while (flagFImArquivo!=""):
          
    nome = arquivo.readline()
    flagFImArquivo=nome
    nome=nome.split("\n")
                
    idade = arquivo.readline()
    idade=idade.split("\n")
                
    altura = arquivo.readline()
    altura=altura.split("\n")

    if (nome[0]!=""):
         aux=[nome[0],int(idade[0]),float(altura[0])]
         dados.append(aux)
         
print("LEITURA DE DADOS EFETUADA COM SUCESSO")       
arquivo.close
        
#IMPRIMINDO DOS DADOS LIDOS
print("IMPRIMINDO O DATASET:")
for pos,vl in enumerate(dados):
    print(pos,"\t",vl)

input("DIGITE ALGO PARA CONTINUAR 6:  ")

#****************************************************************
# 'a': modo de anexar, adiciona informações ao final do arquivo
#****************************************************************
arquivo = open('EXEMPLOTXTCRUD001.txt', 'a')

nome="MOLYBYDENYO"
idade="45"
altura="1.68"

arquivo.writelines(nome+"\n")
arquivo.writelines(idade+"\n")
arquivo.writelines(altura+"\n")
arquivo.close()

# LER DADOS DO ARQUIVO
arquivo = open('EXEMPLOTXTCRUD001.txt', 'r')
print("\nDADOS ATUALIZADOS NO ARQUIVO:")
conteudo=" "
while (conteudo!=""):
    conteudo = arquivo.readline()
    linhas=conteudo.split("\n")
    print("LINHA DADOS: ",linhas[0])
    
arquivo.close()




