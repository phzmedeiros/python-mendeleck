# TITULO DO PROGRAMA
print("**************************************************")
print("************* CONTA DO ChaCoB ********************")
print("**************************************************\n")

# ENTRADA DE DADOS
preco_por_porcao = float(input("Digite o preço da porção (em RP$): "))
num_porcoes = int(input("Digite o número de porções consumidas: "))

# Cálculo do custo base (valor das porções)
custo_base = preco_por_porcao * num_porcoes

# Aplicação do desconto de 2% para cada porção consumida
desconto = custo_base * (0.02 * num_porcoes)
valor_com_desconto = custo_base - desconto

# Adição do couvert artístico
valor_com_couvert = valor_com_desconto + 20.00

# Aplicação de 10% de taxa de serviço
valor_final = valor_com_couvert * 1.10

# SAIDA DE DADOS
print("---------------------------------")
print("--- Detalhamento dos cálculos ---")
print("---------------------------------")
print("\nCusto base (porções): RP$",custo_base)
print("Desconto aplicado: RP$",desconto)
print("Valor após desconto: RP$",valor_com_desconto)
print("Valor com couvert artístico (RP$20,00): RP$",valor_com_couvert)
print("Valor final com taxa de serviço (10%): RP$",valor_final)
