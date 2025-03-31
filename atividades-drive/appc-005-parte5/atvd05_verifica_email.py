print("****************************************")
print("** VERIFICAÇÃO DE EMAIL - Ç3PÓ-2S2 **")
print("****************************************")

frase = input("\nDigite uma frase: ")

if "@" in frase:
    print("\nA frase contém um possível email.")
else:
    print("\nA frase NÃO contém um email.")
