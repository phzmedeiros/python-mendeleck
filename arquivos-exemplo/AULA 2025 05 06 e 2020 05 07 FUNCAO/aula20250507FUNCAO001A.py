# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#DEFINIR UMA FUNCAO PARA
#CALCULO DA MEDIA DE 
#DUAS NOTAS
#OBJETIVOS: AVALIAR CONCEITO
# DE VARIAVEL LOCAL E GLOBAL

#VARIAVEL GLOBAL
soma=110

#n1,n2,soma,md SAO VARIAVEIS
#    LOCAL, ACESSO SOMENTE
#    INTERNAMENTE A FUNCAO
def media(n1,n2):
    soma=n1+n2
    md=soma/2
    return md

vlMedia=media(8,10)
print("MEDIA:  ",vlMedia)

vlMedia=media(10,6)
print("MEDIA:  ",vlMedia)

vlMedia=media(2,4)
print("MEDIA:  ",vlMedia)


print("SOMA:  ",soma)















