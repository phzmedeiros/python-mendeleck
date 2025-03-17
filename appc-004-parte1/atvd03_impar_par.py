# TITULO DO PROGRAMA
print("************************************")
print("*** CLASSIFICAÇÃO - IMPAR OU PAR ***")
print("************************************")

# ENTRADA DE DADOS
numero = int(input("Digite um número: "))

# CONDICIONAL PARA VERIFICAÇÃO DE PARIDADE E RESPOSTA DO PROGRAMA
if numero % 2 == 0:
    resultado = "Par"
else:
    resultado = "Ímpar"

# SAIDA DE DADOS CONCATENANDO COM O PRINT
print(f"O número {numero} é {resultado}.")