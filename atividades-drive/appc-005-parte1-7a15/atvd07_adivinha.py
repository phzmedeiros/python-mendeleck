import random
numero_secreto = random.randint(0, 100)

print("*****************************")
print("**** Jogo da Adivinhação ****")
print("*****************************")

tentativas = -1

while tentativas != numero_secreto:
    tentativas = int(input("\nDigite um número entre 0 e 100: "))

    if tentativas < numero_secreto:
        print("\nO número secreto é maior!")
    if tentativas > numero_secreto:
        print("\nO número secreto é menor!") 
    if tentativas == numero_secreto:
        print("\nParabéns! Você acertou o número secreto!") 
