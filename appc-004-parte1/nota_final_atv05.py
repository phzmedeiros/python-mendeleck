# CÁLCULO DA MÉDIA PONDERADA
print("**********************************")
print("*** CÁLCULO DA MÉDIA PONDERADA ***")
print("**********************************\n")

# ENTRADA DAS NOTAS E PESOS
prova_1 = float(input("Digite a nota da Prova 1: "))
prova_2 = float(input("Digite a nota da Prova 2: "))
peso_1 = float(input("Digite o peso da Prova 1: "))
peso_2 = float(input("Digite o peso da Prova 2: "))

# CÁLCULO DA MÉDIA
media = (prova_1 * peso_1 + prova_2 * peso_2) / (peso_1 + peso_2)

# EXIBIÇÃO DO RESULTADO
print("\n***********************")
print("*** RESULTADO FINAL ***")
print("***********************")
print("Média Final:", media,"\n")

# CONDICIONAL PARA APROVAÇÃO
if media < 5:
    print("REPROVADO")
elif media >= 5:
    print("APROVADO")
elif media >= 8 and media < 9:
    print("PARABÉNS O DESEMPENHO FOI MUITO BOM")
elif media >= 9:
    print("PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR")
