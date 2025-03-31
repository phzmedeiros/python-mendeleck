print("*****************************************")
print("** INVERSÃO E SUBSTITUIÇÃO - LUXLEXYTHOR **")
print("*****************************************")

palavra = input("\nDigite uma palavra: ")

invertida = palavra[::-1]
vogais = "aeiouAEIOU"

substituida_vogal = ""
substituida_a = ""

for letra in palavra:
    if letra in vogais:
        substituida_vogal += "#"
    else:
        substituida_vogal += letra

    if letra == "A" or letra == "a":
        substituida_a += "$"
    else:
        substituida_a += letra

# Resultados
print(f"\nPalavra invertida: {invertida}")
print(f"Vogais substituídas por #: {substituida_vogal}")
print(f"Letras 'A' substituídas por $: {substituida_a}")
