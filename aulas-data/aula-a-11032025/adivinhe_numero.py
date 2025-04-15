# IMPORTAÇÃO DE BIBLIOTECA RANDOM PARA GERAR NÚMERO ALEATÓRIO
import random

# GERAÇÃO DE NÚMERO ALEATÓRIO ENTRE 0 E 100
numero_secreto=random.randint(0,100)

# DEFINIÇÃO DE VARIÁVEL PARA ARMAZENAR O NÚMERO DO JOGADOR FORA DE 0 PORQUE O NÚMERO 0 É VÁLIDO
numero_jogador = -1

# MENSAGEM DE INÍCIO DO JOGO
print("JOGO - ADIVINHE O NÚMERO (0 a 100)\n")

# LAÇO DE REPETIÇÃO PARA O JOGADOR DIGITAR O NÚMERO ATÉ ACERTAR O NÚMERO SECRETO
while numero_jogador != numero_secreto:
    # TENTATIVA DO JOGADOR DIGITAR O NÚMERO
    numero_jogador = int(input("DIGITE UM NÚMERO: "))
    # CONDIÇÕES PARA O JOGADOR SABER SE O NÚMERO É MAIOR, MENOR OU IGUAL AO NÚMERO SECRETO
    if(numero_jogador > numero_secreto):
        print("O seu número é MAIOR que o do computador")
    if(numero_jogador < numero_secreto):
        print("O seu número é MENOR que o do computador")  
    if(numero_jogador == numero_secreto):
        print("\nPARABÉNS, VOCÊ ACERTOU O NÚMERO SECRETO!!!")
