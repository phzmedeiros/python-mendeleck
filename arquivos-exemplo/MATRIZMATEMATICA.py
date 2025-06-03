# -*- coding: utf-8 -*-
"""
Created on Sun May 11 08:10:32 2025

@author: AM2
"""



matriz1=[
    [5,5,3,2],
    [3,6,4,2],
    [2,1,4,1],
    [6,7,1,2]
    ]

matriz2=[
    [6,3,3,1],
    [2,4,5,6],
    [1,0,4,2],
    [9,1,1,3]
    ]

matriz3=[
    [2,3,0],
    [6,5,4],
    [3,4,5],
    [1,2,3]
    ]

identidade=[
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
    ]

def printMatriz(rotulo,m):
    tamLin1=len(m)
    tamCol1=len(m[0])
    print("\n",rotulo)
    for lin in range(tamLin1):
        aux=""
        for col in range(tamCol1):
            aux=aux+format(m[lin][col],"8.2f")
        print(aux)    

#************************             
#***** SOMAR MATRIZ *****
#************************ 
#ATENCAO: MATRIZES TEM QUE TER A MESMA ORDEM 
def somarMatriz(m1,m2):
    matrizResultado=[]
    
    tamLin1=len(m1)
    tamCol1=len(m1[0])

    tamLin2=len(m2)
    tamCol2=len(m2[0])

    #VERIFICAR ORDEM DAS MATRIZES
    #MATRIZ m1 e m2 DEVEM TER A MESMA ORDEM
    #OU SEJA, NUMERO DE LINHAS E COLUNAS, 
    #DAS DUAS MATRIZES, DEVEM SER IGUAIS
    if (tamLin1!=tamLin2)or(tamCol1!=tamCol2):
        return None
    
    for lin in range(tamLin1):
        aux=[]
        for col in range(tamCol1):
            soma=m1[lin][col]+m2[lin][col]
            aux.append(soma)
            
        #ACRESCENTAR LINHA NA MATRIZ RESULTADO    
        matrizResultado.append(aux)    
           
    return matrizResultado

#***************************             
#***** SUBTRAIR MATRIZ *****
#*************************** 
#ATENCAO: MATRIZES TEM QUE TER A MESMA ORDEM 
def subtrairMatriz(m1,m2):
    matrizResultado=[]
    
    tamLin1=len(m1)
    tamCol1=len(m1[0])

    tamLin2=len(m2)
    tamCol2=len(m2[0])

    #VERIFICAR ORDEM DAS MATRIZES
    #MATRIZ m1 e m2 DEVEM TER A MESMA ORDEM
    #OU SEJA, NUMERO DE LINHAS E COLUNAS, 
    #DAS DUAS MATRIZES, DEVEM SER IGUAIS
    if (tamLin1!=tamLin2)or(tamCol1!=tamCol2):
        return None
    
    for lin in range(tamLin1):
        aux=[]
        for col in range(tamCol1):
            soma=m1[lin][col]-m2[lin][col]
            aux.append(soma)
            
        #ACRESCENTAR LINHA NA MATRIZ RESULTADO    
        matrizResultado.append(aux)    
           
    return matrizResultado


#******************************
#***** MULTIPLICAR MATRIZ *****
#******************************
def multiplicarMatriz(m1,m2):
    matrizResultado=[]
    
    tamLin1=len(m1)
    tamCol1=len(m1[0])

    tamLin2=len(m2)
    tamCol2=len(m2[0])

    #VERIFICAR ORDEM DAS MATRIZES
    #MATRIZ m1 e m2 DEVEM TER ORDEM COMPATIVEL
    #OU SEJA, NUMERO DE COLUNAS DE m1 
    #         DEVE SER IGUAL AO NUMERO DE LINHAS DE m2
    if (tamCol1!=tamLin2):
        return None
    
    for lin in range(tamLin1):
        aux=[]
        for col in range(tamCol2):
            soma=0
            for s in range(tamLin2):
                soma=soma+m1[lin][s]*m2[s][col]
            
            aux.append(soma)
            
        #ACRESCENTAR LINHA NA MATRIZ RESULTADO    
        matrizResultado.append(aux)    
           
    return matrizResultado

#*****************************
#***** TRANSPOSTA MATRIZ *****
#*****************************
def transpostaMatriz(m):
    matrizResultado=[]
    
    tamLin=len(m)
    tamCol=len(m[0])

    for col in range(tamCol):
        aux=[]
        for lin in range(tamLin):
            aux.append(m[lin][col])
            
        matrizResultado.append(aux)
           
    return matrizResultado

#***********************************
#***** GERAR MATRIZ IDENTIDADE *****
#***********************************
def identidadeMatriz(ordem):
    matrizResultado=[]

    for lin in range(ordem):
        aux=[]
        for col in range(ordem):
            if (lin==col):
                aux.append(1)
            else:
                aux.append(0)
            
        matrizResultado.append(aux)
           
    return matrizResultado



#**************************
#***** INVERSA MATRIZ *****
#***** METODO DO PIVO *****
#**************************
#    ORIGINAL   INVERSA
#   | 1 2 3 4 | 1 0 0 0 |
#   | 5 6 7 8 | 0 1 0 0 |
#   | 9 0 1 2 | 0 0 1 0 |
#   | 3 4 5 6 | 0 0 0 1 |
#
# APLICANDO METODO
#    ORIGINAL   INVERSA
#   | 1 0 0 0 | a b c d |
#   | 0 1 0 0 | e f g h |
#   | 0 0 1 0 | i j k l |
#   | 0 0 0 1 | m n o p |
#**************************
def inversaMatriz(m):
    mAux=[]
    
    tamLin=len(m)
    tamCol=len(m[0])

    #COPIAR MATRIZ ORIGINAL
    for lin in range(tamLin):
        aux=[]
        for col in range(tamCol):
            aux.append(m[lin][col])
        mAux.append(aux)    
           
    if (tamLin!=tamCol):
        return None
        
    matrizResultado=identidadeMatriz(tamLin)
    
    #PIVO DOWN
    for p in range(tamLin):
        pivo=mAux[p][p]

        for lin in range(p+1,tamLin):
            auxCol=mAux[lin][p]
            for col in range(0,tamCol):
                mAux[lin][col]=mAux[p][col]/pivo*(-auxCol)+mAux[lin][col]
                matrizResultado[lin][col]=matrizResultado[p][col]/pivo*(-auxCol)+matrizResultado[lin][col]
 
    
    #PIVO UP
    for p in range(tamLin-1,-1,-1):
        pivo=mAux[p][p]
        for lin in range(p-1,-1,-1):
            auxCol=mAux[lin][p]
            for col in range(tamCol-1,-1,-1):
                mAux[lin][col]=mAux[p][col]/pivo*(-auxCol)+mAux[lin][col]
                matrizResultado[lin][col]=matrizResultado[p][col]/pivo*(-auxCol)+matrizResultado[lin][col]
            
    #DIAGONAL - DIVIDIR LINHAS PELO PIVO
    for lin in range(tamLin):
        fator=mAux[lin][lin]
        for col in range(tamCol):
            mAux[lin][col]=mAux[lin][col]/fator
            matrizResultado[lin][col]=matrizResultado[lin][col]/fator
          
    return matrizResultado



printMatriz("MATRIZ 1",matriz1)
printMatriz("MATRIZ 2",matriz2)

matriz1MAISmatriz2=somarMatriz(matriz1, matriz2)
printMatriz("SOMA: MATRIZ 1 + MATRIZ 2",matriz1MAISmatriz2)

matriz1MENOSmatriz2=subtrairMatriz(matriz1, matriz2)
printMatriz("SUBTRAIR: MATRIZ 1 + MATRIZ 2",matriz1MENOSmatriz2)

matriz1VEZESmatriz2=multiplicarMatriz(matriz1, matriz2)
printMatriz("MULTIPLICAR: MATRIZ 1 * MATRIZ 2",matriz1VEZESmatriz2)

TRANSPOSTAmatriz1=transpostaMatriz(matriz1)
printMatriz("TRANSPOSTA: MATRIZ 1",TRANSPOSTAmatriz1)

printMatriz("MATRIZ 3",matriz3)
TRANSPOSTAmatriz3=transpostaMatriz(matriz3)
printMatriz("TRANSPOSTA: MATRIZ 3",TRANSPOSTAmatriz3)

printMatriz("IDENTIDADE: MATRIZ",identidadeMatriz(4))

INVERSAmatriz1=inversaMatriz(matriz1)
printMatriz("INVERSA: MATRIZ 1",INVERSAmatriz1)

#TESTAR MATRIZ INVERSA
matrizInversa1VEZESmatriz1=multiplicarMatriz(INVERSAmatriz1, matriz1)
printMatriz("MULTIPLICAR: INVERSA 1 * MATRIZ 1",matrizInversa1VEZESmatriz1)