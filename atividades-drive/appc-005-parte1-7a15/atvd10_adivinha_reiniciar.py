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
        print("O número secreto é maior!")
    if tentativa > numero_secreto:
        print("O número secreto é menor!") 
    if tentativa == numero_secreto:
        print(f"\nParabéns! Você acertou o número secreto em {count} tentativas!")
    print("\nDeseja desistir da partida? (s/n)")
    desistir = input()
    if desistir == "s":
        print(f"\nO número secreto era {numero_secreto}")
        tentativa = numero_secreto

        print("\nDeseja iniciar uma nova partida? (s/n)")
        nova_partida = input()
        if nova_partida == "s":
            count = 0
            tentativa = -1
            numero_secreto = random.randint(0, 100)
            print("\nUma nova partida foi iniciada! Boa sorte!")
        else:
            print("\nObrigado por jogar! Até a próxima!")
            tentativa = numero_secreto