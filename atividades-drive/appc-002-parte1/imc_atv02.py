# TITULO DO PROGRAMA
print("**************************************************")
print("*************CALCULADORA DE IMC*******************")
print("**************************************************")

# ENTRADA DE DADOS - ALTURA E PESO
altura = float(input("\nDigite sua altura em metros: "))
peso = float(input("\nDigite seu peso em quilogramas: "))

# CALCULO DO IMC
imc = peso / (altura * altura)

# TITULO DA SAIDA DE DADOS
print("\n\n*************************************************")
print("*********RESULTADO DO CALCULO DO IMC*************")
print("*************************************************")
# SAIDA DE DADOS - IMC
print("\nSua altura é: ",altura,"m")
print("\nSeu peso é: ",peso,"Kg")
print("\nSeu Indice de Massa Corporal é: ",imc,"\n\n")