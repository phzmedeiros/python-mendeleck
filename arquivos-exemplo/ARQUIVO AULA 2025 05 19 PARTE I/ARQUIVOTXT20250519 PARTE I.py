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
arquivo = open('EXEMPLOTXT000.txt', 'r')


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

# IMPRIMIR POR CARACTER
print("\nIMPRIMIR CARACTERES:")
for i in conteudo:
    print(i)

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
    
#******************************************
# OUTRA ABORDAGEM PARA ABERTURA DO ARQUIVO
#******************************************
arquivo = open('EXEMPLOTXT000.txt', 'r')
print("\n\nOUTRA ABORDAGEM PARA A LEITURA DOS DADOS DO ARQUIVO")
conteudo=" "
while (conteudo!=""):
    conteudo = arquivo.read(1)
    print(conteudo,end="")
    
arquivo.close()



#************************************************************
#  CRIANDO O PONTEIRO PARA UM ARQUIVO - ESCREVER NO ARQUIVO
#************************************************************
# 'w': modo de escrita, se o arquivo não existir, ele será criado
arquivo = open('EXEMPLOTXT000b.txt', 'w')

texto1="JUVENAL E PERCIVAL SAO AMIGOS"
texto2="JUVENAL ESTUDA NA PUC-CAMPINAS"
texto3="PERCIVAL ESTUDA NA PUC-RAPIDOPOLIS"
texto4="FIM"

arquivo.writelines(texto1+'\n')
arquivo.writelines(texto2+'\n')
arquivo.writelines(texto3+'\n')
arquivo.writelines(texto4+'\n')

arquivo.close()

#LENDO OS DADOS GRAVADOS
arquivo = open('EXEMPLOTXT000b.txt', 'r')

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


#***************************************************************
# OUTRA ABORDAGEM PARA ABERTURA DO ARQUIVO - LEITURA POR LINHA
#***************************************************************
arquivo = open('EXEMPLOTXT000b.txt', 'r')
print("\n\nOUTRA ABORDAGEM PARA A")
print("LEITURA DOS DADOS DO ARQUIVO")
print("LEITURA POR LINHA:\n")
conteudo=" "
while (conteudo!=""):
    conteudo = arquivo.readline()
    print(conteudo)
    
arquivo.close()


#***************************************************************
# OUTRA ABORDAGEM PARA ABERTURA DO ARQUIVO - LEITURA POR LINHA
#***************************************************************
arquivo = open('EXEMPLOTXT000b.txt', 'r')
print("\n\nOUTRA ABORDAGEM PARA A")
print("LEITURA DOS DADOS DO ARQUIVO")
print("LEITURA POR LINHA:")
conteudo=" "
while (conteudo!=""):
    conteudo = arquivo.readline()
    print("\nCONTEUDO:    ",conteudo)
    linhas=conteudo.split("\n")
    print("LINHAS:      ",linhas)
    print("LINHA DADOS: ",linhas[0])
    
arquivo.close()


#*******************************************
#  CRIANDO O PONTEIRO PARA UM ARQUIVO
#*******************************************
arquivo = open('EXEMPLOTXT000b.txt', 'r')
print("\n\nDADOS ORIGINAIS CADASTRADOS NO ARQUIVO:")
conteudo=" "
while (conteudo!=""):
    conteudo = arquivo.readline()
    linhas=conteudo.split("\n")
    print("LINHA DADOS: ",linhas[0])
    
arquivo.close()

#****************************************************************
# 'a': modo de anexar, adiciona informações ao final do arquivo
#****************************************************************
arquivo = open('EXEMPLOTXT000b.txt', 'a')

textoNovaLinha="ACRESCENTANDO UMA LINHA"
arquivo.writelines(textoNovaLinha+'\n')

arquivo.close()

# LER DADOS DO ARQUIVO
arquivo = open('EXEMPLOTXT000b.txt', 'r')
print("\nDADOS ATUALIZADOS NO ARQUIVO:")
conteudo=" "
while (conteudo!=""):
    conteudo = arquivo.readline()
    linhas=conteudo.split("\n")
    print("LINHA DADOS: ",linhas[0])
    
arquivo.close()




