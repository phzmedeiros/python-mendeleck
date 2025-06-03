# -*- coding: utf-8 -*-
"""
Created on Wed May  7 20:58:30 2025

@author: AM2
"""

#Desenvolver uma função e efetuar a implementação em Python,
#para calcular o valor do imposto de renda de acordo com a 
#tabela:
#BASE CALCULO                  ALIQUOTA      DESCONTO     
# BC <= 2259.20                  0.0%           0.00
# 2259.21 <= BC <= 2826.65       7.5%         169.44
# 2826.66 <= BC <= 3751.05      15.0%         381.44
# 3751.06 <= BC <= 4664.68      22.5%         662.47
# BC >= 4664.69                 27.5%         896.00
#
#Retornar o valor da alíquota e do imposto a ser pago.
def calculoIR(basecalculo):
    if (basecalculo<=2259.20):
        aliquota=0
        desconto=0
    elif (basecalculo>=2259.21)and(basecalculo<=2826.65):
        aliquota=7.5
        desconto=169.44
    elif (basecalculo>=2826.66)and(basecalculo<=3751.05):
        aliquota=15
        desconto=381.44
    elif (basecalculo>=3751.06)and(basecalculo<=4664.68):
        aliquota=22.5
        desconto=662.47
    else:
        aliquota=27.5
        desconto=896.00        
            
    vlIR=basecalculo*aliquota/100-desconto
    return aliquota,vlIR



salario=1000.00
alq,valorimposto=calculoIR(salario)
print("\nSALARIO:       ",format(salario,"10.2f"))
print("ALIQUOTA:      ",format(alq,"10.2f"))
print("IMPOSTO RENDA: ",format(valorimposto,"10.2f"))

salario=3000.00
alq,valorimposto=calculoIR(salario)
print("\nSALARIO:       ",format(salario,"10.2f"))
print("ALIQUOTA:      ",format(alq,"10.2f"))
print("IMPOSTO RENDA: ",format(valorimposto,"10.2f"))

salario=4000.00
alq,valorimposto=calculoIR(salario)
print("\nSALARIO:       ",format(salario,"10.2f"))
print("ALIQUOTA:      ",format(alq,"10.2f"))
print("IMPOSTO RENDA: ",format(valorimposto,"10.2f"))

salario=5000.00
alq,valorimposto=calculoIR(salario)
print("\nSALARIO:       ",format(salario,"10.2f"))
print("ALIQUOTA:      ",format(alq,"10.2f"))
print("IMPOSTO RENDA: ",format(valorimposto,"10.2f"))

salario=10000.00
alq,valorimposto=calculoIR(salario)
print("\nSALARIO:       ",format(salario,"10.2f"))
print("ALIQUOTA:      ",format(alq,"10.2f"))
print("IMPOSTO RENDA: ",format(valorimposto,"10.2f"))

