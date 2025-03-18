# TITULO DO PROGRAMA
print("*************************")
print("**  CALCULO DE CÂMBIO  **")
print("*************************\n")

# ENTRADA DE DADOS - Cotação do RAPID em relação ao Dólar e volume de dólar a ser comprado
cotacao = float(input("Digite a cotação do RAPID em relação ao Dólar: RP$"))
volume_dolar = float(input("Digite o volume de dólar a ser comprado: $"))

# Cálculo da conversão de valores
valor_convertido = volume_dolar * cotacao

# Aplicação do acréscimo de R$ 10,00
valor_com_acrescimo = valor_convertido + 10

# Aplicação de 2% de taxa de administração
valor_com_taxa_adm = valor_com_acrescimo + (valor_com_acrescimo * 0.02)

# Aplicação de 0.6% de imposto de renda
valor_final = valor_com_taxa_adm + (valor_com_taxa_adm * 0.006)

# SAIDA DE DADOS
print("\nResultado da operação de câmbio:")
print("Valor final: RP${:.2f}".format(valor_final))