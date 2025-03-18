# Programa de Cálculo de Desconto do IPTU
print("***********************")
print("** CÁLCULO DE IPTU **")
print("***********************")

# Leitura dos dados
ano_construcao = int(input("Digite o ano de construção do imóvel: "))
ano_atual = int(input("Digite o ano atual: "))

# Cálculo da idade do imóvel
idade = ano_atual - ano_construcao

# Determinação do percentual de desconto
if idade < 5:
    desconto = 0
elif idade >= 5 and idade < 20:
    desconto = 15
elif idade >= 20 and idade < 40:
    desconto = 25
else:
    desconto = 30

# Exibição dos resultados
print("\n*************************")
print("** RESULTADO DO CÁLCULO **")
print("*************************")
print("Idade do imóvel:", idade, "anos")
print("Percentual de desconto do IPTU:", desconto, "%")