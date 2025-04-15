palavra = "GUARANY CAMPEAO"
letra_remover = 'A'

resultado = ""
i = 0
while i < len(palavra):
    if palavra[i] != letra_remover:
        resultado = resultado + palavra[i]
    i = i + 1

print(resultado)
