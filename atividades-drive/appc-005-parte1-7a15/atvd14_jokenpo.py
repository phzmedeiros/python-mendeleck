import random

print("***********************************")
print("** Bem-vindo ao jogo de Jokenpô! **")
print("***********************************")
print("Escolha sua jogada:")
print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")
usuario = int(input("\nDigite sua escolha (0, 1 ou 2): "))

opcoes = ["Pedra", "Papel", "Tesoura"]
computador = random.randint(0, 2)

print(f"\nVocê escolheu: {opcoes[usuario]}")
print(f"O computador escolheu: {opcoes[computador]}")

if usuario == computador:
    print("Empate!")
elif (usuario == 0 and computador == 2) or (usuario == 1 and computador == 0) or (usuario == 2 and computador == 1):
    print("Você venceu!")
else:
    print("Você perdeu!")
