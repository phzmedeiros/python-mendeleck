# TITULO DO PROGRAMA
print("***********************************************")
print("******CALCULADORA DE MEDIAS RAPIDOPOLENSE******")
print("***********************************************")

# ENTRADA DE DADOS DO PROGRAMA
nota_um = float(input("\nDigite a primeira nota = "))
nota_dois = float(input("\nDigite a segunda nota = "))

# CALCULO DA MEDIA DO ALUNO
media = (nota_um + nota_dois)/2

# TITULO PARA EXIBIÇÃO DE RESULTADOS
print("\n\n************************************************")
print("*******RESULTADOS RAPIDOPOLENSES DO ALUNO*******")
print("************************************************")

# SAIDA DE DADOS COM A MEDIA DO ALUNO E SUAS RESPECTIVAS NOTAS
print("\nPrimeira nota do aluno = ",nota_um)
print("\nSegunda nota do aluno = ",nota_dois)
print("\nMedia do aluno = ",media)

# CONDIÇÃO DE APROVAÇÃO E SAIDA DE DADOS DO RESULTADO DO ALUNO
if (media >= 5):
    print("\n*******************************")
    print("***Aluno aprovado!! Congrats***")
    print("*******************************")
if (media < 5):
    print("\n**********************")
    print("***Aluno reprovado!***")
    print("**********************")