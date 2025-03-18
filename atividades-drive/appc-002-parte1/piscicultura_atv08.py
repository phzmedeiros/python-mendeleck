# TITULO DO PROGRAMA
print("******************************************************")
print("*** CÁLCULO DA MÉDIA PONDERADA DA MASSA DOS PEIXES ***")
print("******************************************************")

# ENTRADA DE DADOS - MASSA E COMPRIMENTO DOS PEIXES
massa_peixe_1 = float(input("\nDigite a massa do peixe 1 em kg: "))
comprimento_peixe_1 = float(input("Digite o comprimento do peixe 1 em cm: "))

massa_peixe_2 = float(input("\nDigite a massa do peixe 2 em kg: "))
comprimento_peixe_2 = float(input("Digite o comprimento do peixe 2 em cm: "))

massa_peixe_3 = float(input("\nDigite a massa do peixe 3 em kg: "))
comprimento_peixe_3 = float(input("Digite o comprimento do peixe 3 em cm: "))

massa_peixe_4 = float(input("\nDigite a massa do peixe 4 em kg: "))
comprimento_peixe_4 = float(input("Digite o comprimento do peixe 4 em cm: "))

massa_peixe_5 = float(input("\nDigite a massa do peixe 5 em kg: "))
comprimento_peixe_5 = float(input("Digite o comprimento do peixe 5 em cm: "))

massa_peixe_6 = float(input("\nDigite a massa do peixe 6 em kg: "))
comprimento_peixe_6 = float(input("Digite o comprimento do peixe 6 em cm: "))

massa_peixe_7 = float(input("\nDigite a massa do peixe 7 em kg: "))
comprimento_peixe_7 = float(input("Digite o comprimento do peixe 7 em cm: "))

# CÁLCULO DA SOMA PONDERADA DE MASSA E COMPRIMENTO DOS PEIXES
soma_ponderada = (massa_peixe_1 * comprimento_peixe_1 +
                  massa_peixe_2 * comprimento_peixe_2 +
                  massa_peixe_3 * comprimento_peixe_3 +
                  massa_peixe_4 * comprimento_peixe_4 +
                  massa_peixe_5 * comprimento_peixe_5 +
                  massa_peixe_6 * comprimento_peixe_6 +
                  massa_peixe_7 * comprimento_peixe_7)

# CÁLCULO DA SOMA DOS COMPRIMENTOS PARA A MÉDIA PONDERADA
soma_comprimentos = (comprimento_peixe_1 + comprimento_peixe_2 + 
                     comprimento_peixe_3 + comprimento_peixe_4 + 
                     comprimento_peixe_5 + comprimento_peixe_6 +  comprimento_peixe_7)

# CÁLCULO DA MÉDIA PONDERADA
media_ponderada = soma_ponderada / soma_comprimentos

# SAÍDA DE DADOS
print("\n********************************************************")
print(f"*** A média ponderada da massa dos peixes é: {media_ponderada:.2f}kg ***")
print("********************************************************")
