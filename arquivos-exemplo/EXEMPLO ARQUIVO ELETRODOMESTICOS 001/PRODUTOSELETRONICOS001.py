# -*- coding: utf-8 -*-
"""
Created on Wed May 21 20:04:38 2025

@author: AM2
"""

#DESENVOLVER UMA APLICACAO DE SOFTWARE PARA 
# GESTAO DO ESTOQUE DE PRODUTOS ELETROELETRONICOS
# DA VAREJISTA ONLINE  MERCADAO RAPIDOPOLIS.
# A ESTRUTURA DO ARQUIVO EH A SEGUINTE:
#         NOME DO PRODUTO
#         QUANTIDADE NO ESTOQUE
#         PRECO UNITARIO
# O SOFTWARE DEVE INCORPORAR AS SEGUINTES FUNCIONALIDADES
# QUE DEVEM SER IMPLEMENTADAS ATRAVES DE FUNCOES:
#     LISTAR OS DADOS CADASTRADOS E CADASTRAR EM UMA LISTA
#     CALCULAR O CUSTO DO ESTOQUE POR PRODUTO
#     CALCULAR O CUSTO TOTAL DO ESTOQUE
    

DATASET001=[]

#EFETUAR A LEITURA DOS DADOS NO ARQUIVO
#ENTRADA:
#  NOME DO ARQUIVO
#
#SAIDA:
#  LISTA COM OS DADOS 
#       [NOME PRODUTO, QUANTIDADE, PRECO UNITARIO]
def lerDadosArquivo(nomearquivo):
    auxDataset=[]
    arquivo=open(nomearquivo,"r")
    aux=" "
    while(aux!=""):
        #LER NOME PRODUTO
        aux=arquivo.readline()
        dados=aux.split("\n")
        nomeProduto=dados[0]

        if (aux!=""):
            #LER QUANTIDADE NO ESTOQUE
            aux=arquivo.readline()
            dados=aux.split("\n")
            quantidade=int(dados[0])
    
            #LER PRECO UNITARIO
            aux=arquivo.readline()
            dados=aux.split("\n")
            precoUnitario=float(dados[0])
            
            auxDataset.append([nomeProduto,quantidade,precoUnitario])

    return auxDataset

#LISTAR OS DADOS DO DATASET
#ENTRADA:
#   DATASET
#SAIDA:
#    
def listarDataset(ds):
    print("\n\n*********************")
    print("DATASET:")
    print("*********************")
    for i in ds:
        print(i)
   
#LISTAR OS DADOS DO DATASET
#ENTRADA:
#   DATASET
#SAIDA:
#    
def listarDatasetDetalhado(ds):
    print("\n\n*********************")
    print("DATASET DETALHADO:")
    print("*********************")
    for i in ds:
        print("\nNOME PRODUTO:       ",i[0])
        print("QUANTIDADE ESTOQUE: ",format(i[1],"7d"))
        print("PRECO UNITARIO:  R$ ",format(i[2],"10.2f"))
        
#CALCULAR O CUSTO DO ESTOQUE POR PRODUTO
#ENTRADA:
#  DATASET
#
#SAIDA:
#  LISTA COM OS DADOS 
#       [NOME PRODUTO, QUANTIDADE, PRECO UNITARIO, CUSTO TOTAL]
def calcularCustoProdutoEstoque(ds):
    auxDataset=[]
    total=0
    for i in ds:
        custo=i[1]*i[2]
        aux=[i[0],i[1],i[2],custo]
        auxDataset.append(aux)
        total=total+custo
    return total,auxDataset    
        
#LISTAR CUSTO DOS PRODUTOS
#ENTRADA:
#   DATASET
#SAIDA:
#    
def listarCustoProduto(ds):
    print("\n\n*********************")
    print("CUSTO POR PRODUTO:")
    print("*********************")
    for i in ds:
        print("\nNOME PRODUTO:       ",i[0])
        print("QUANTIDADE ESTOQUE: ",format(i[1],"7d"))
        print("PRECO UNITARIO:  R$ ",format(i[2],"10.2f"))
        print("VALOR DO ESTOQUE R$ ",format(i[3],"10.2f"))
        

#LER DADOS DO ARQUIVO E ARMAZENAR NO DATASET
DATASET001=lerDadosArquivo("ELETRODOMESTICOS001.txt")

#LISTRAR DADOS DO DATASET001
listarDataset(DATASET001)

#LISTAR DADOS DO DATASET001 - DETALHES
listarDatasetDetalhado(DATASET001)

#CALCULAR CUSTO DO ESTOQUE - POR PRODUTO
DATASETCUSTOPRODUTO=[]
custoEstoque,DATASETCUSTOPRODUTO=calcularCustoProdutoEstoque(DATASET001)

#LISTAR CUSTO PRODUTO
listarCustoProduto(DATASETCUSTOPRODUTO)
print("\n\n******** CUSTO TOTAL DO ESTOQUE  R$ ",format(custoEstoque,"10.2f"))






