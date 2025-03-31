import random

print("**************************************")
print("** JOGO DA PALAVRA SECRETA **")
print("**************************************")

palavras = ["JUVENAL", "LARANJA", "UVA", "COMPUTACAO", "LESMA", "GUARANY"]
secreta = random.choice(palavras)
acertos = ["*"] * len(secreta)
tentativas = 0

while "*" in acertos:
    print("\nPALAVRA: ", acertos)
    letra = input("Digite uma letra: ").upper()
    tentativas += 1

    for i in range(len(secreta)):
        if secreta[i] == letra:
            acertos[i] = letra

print(f"\nParabéns! Você acertou a palavra '{secreta}' em {tentativas} tentativas!")
