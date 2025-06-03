# -*- coding: utf-8 -*-
"""
Spyder Editor
AULA20250528WRITE005 B
This is a temporary script file.
"""

#DESENVOLVER UMA APLICACAO DE SOFTWARE,
#EM PYTHON, PARA LER OS DADOS ATRAVES DO TECLADO
#E GRAVAR NO ARQUIVO
#DADOS:   PRODUTO   QUANTIDADE   PRECOUNITARIO    
#APOS A GRAVACAO DE UM REGISTRO, PERGUNTAR
#  SE DESEJA OUTRO CADASTRO
#GRAVAR OS DADOS NO ARQUIVO
arq=open("EMBELEZZA005.TXT","w")
while (True):
    produto=      input("\nPRODUTO:        ")
    quantidade=   float(input("QUANTIDADE:     "))
    precounitario=float(input("PRECO UNITARIO: "))
    aux=format(produto,"20s")+"|"+format(quantidade,"6.2f")+"|"+format(precounitario,"10.2f")                                       
    arq.writelines(aux+"\n")
    
    op=input("DESEJA OUTRO CADATRO <S/N> ?")
    if (op=="N")or(op=="n"):
        break
arq.close()

