nivel = input("Informe o nível de fidelidade do cliente: ")

if nivel == "gold":
    porcentagem = 5
elif nivel == "platinum":
    porcentagem = 10
elif nivel == "infinity":
    porcentagem = 20
else:
    porcentagem = 0

print(f"O valor correspondente é: {porcentagem}%")