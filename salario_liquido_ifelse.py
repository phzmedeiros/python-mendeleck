# TITULO DO PROGRAMA
print("**************************************************")
print("***CALCULADORA DE SALARIO LIQUIDO RAPIDOPOLENSE***")
print("**************************************************")

# ENTRADA DE DADOS - HORAS E SALARIO HORA
salario_hora = float(input("\nDigite o valor correspondente a uma hora trabalhada = "))
horas_trabalhadas = float(input("\nDigite a quantidade de horas trabalhadas = "))

# CALCULO DO SALARIO BRUTO E DEFINIÇÃO DA VARIAVEL GLOBAL PIR
salario_bruto = salario_hora * horas_trabalhadas
PIR = 0

# ESTRUTURA DE DECISÃO PARA DEFINIÇÃO DA PERCENTAGEM DO PIR
if (salario_bruto < 1000):
    PIR = 0.1
if (salario_bruto >= 1000) and (salario_bruto<3000):
    PIR = 0.15
if (salario_bruto>=3000):
    PIR = 0.225

# DEFINIÇÃO DO DESCONTO
desconto_renda = salario_bruto * PIR

# CALCULO DO SALARIO LIQUIDO
salario_liquido = salario_bruto - desconto_renda

# SAIDA DE DADOS
print("\n**************************************************")
print("\nO correspondente salário bruto é R$",salario_bruto)
print("\nO valor total do salário liquido é R$",salario_liquido)