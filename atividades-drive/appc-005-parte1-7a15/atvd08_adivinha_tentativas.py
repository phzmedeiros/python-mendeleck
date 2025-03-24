import random
numero_secreto = random.randint(0, 100)

print("*****************************")
print("**** Jogo da Adivinhação ****")
print("*****************************")
count = 0
tentativa = -1

while tentativa != numero_secreto:
    tentativa = int(input("\nDigite um número entre 0 e 100: "))
    count = count + 1
    if tentativa < numero_secreto:
        print("\nO número secreto é maior!")
    if tentativa > numero_secreto:
        print("\nO número secreto é menor!") 
    if tentativa == numero_secreto:
        print(f"\nParabéns! Você acertou o número secreto em {count} tentativas!")
