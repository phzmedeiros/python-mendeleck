# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 08:18:32 2025

@author: p226646
"""

nome="ADERBAL"

print("\nREPETICAO COM WHILE")
cont =0
while(cont<7):
    print("CONTADOR: ",cont,"\t",nome[cont])
    cont=cont+1
 
    
print("\nREPETICAO COM FOR")
for cont2 in range(0,7):
    print("CONTADOR: ",cont2,"\t",nome[cont2])
    
print("\nREPETICAO COM FOR 2")  
for cont3 in nome:    
    print(cont3)
    
    
    
    
    