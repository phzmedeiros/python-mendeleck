# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 21:39:48 2025

@author: AM2
"""

# A editora LUXLEXYTHOR, gestora do dicionário horélyuz, 
# está solicitando a você, que desenvolva uma aplicação 
# de software para ler uma palavra, através do teclado, 
# e realize as seguintes operações:
#
# Inverta a ordem das letras, onde a primeira terá a 
# sua posição troCAda com última, a segunda com a penúltima,  
# e assim por diante:
#
#          Palavra=“JUREMA”
#               PALAVRAINVERTIDA=“AMERUJ”
#
# Substituir todas as vogais por “#”
# Substituir todas as letras “A” pelo SíMBOLO “$”


pl=input("DIGITE A PALAVRA - USAR LETRA MAIUSCULA: ")

#pl="GUARANY"

inverterPL=""
auxPL=""
auxPL_A=""

tam = len(pl)

pos=0
while(pos<tam):
    #INVERTER
    inverterPL=inverterPL+pl[tam-pos-1]
    
    #SUBSTITUIR VOGAL
    if ((pl[pos]=="A")or(pl[pos]=="E")or(pl[pos]=="I")or(pl[pos]=="O")or(pl[pos]=="U")):
        auxPL=auxPL+"#"
    else:
        auxPL=auxPL+pl[pos]

    #SUBSTITUIR VOGAL "A" POR "$"
    if (pl[pos]=="A"):
        auxPL_A=auxPL_A+"$"
    else:
        auxPL_A=auxPL_A+pl[pos]


    pos=pos+1

print("\nPALAVRA: ",pl)


print("\nNUMERO TOTAL DE CARACTERES:  ",tam)
print("PALAVRA INVERTIDA:           ",inverterPL)
print("SUBSTITUIR VOGAL POR #:      ",auxPL)
print("SUBSTITUIR VOGAL [A] POR $:  ",auxPL_A)

