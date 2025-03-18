# CALCULADORA DE SALÁRIO LÍQUIDO
print("****************************************************")
print("*** CALCULADORA DE SALÁRIO LÍQUIDO RAPIDOPOLENSE ***")
print("****************************************************")

# ENTRADA DE DADOS - SALÁRIO HORA E HORAS TRABALHADAS
salario_hora = float(input("\nDigite o valor correspondente a uma hora trabalhada: R$"))
horas_trabalhadas = float(input("\nDigite a quantidade de horas trabalhadas: "))

# CÁLCULO DO SALÁRIO BRUTO
salario_bruto = salario_hora * horas_trabalhadas

# DEFINIÇÃO DOS DESCONTOS
desconto_aposentadoria = salario_bruto * 0.10
desconto_imposto_renda = salario_bruto * 0.05

# CÁLCULO DO SALÁRIO LÍQUIDO
salario_liquido = salario_bruto - (desconto_aposentadoria + desconto_imposto_renda)

# SAÍDA DE DADOS
print("\n\n***********************")
print("*** SOBRE O SALÁRIO ***")
print("***********************")
print("\nO correspondente salário bruto é R$",salario_bruto)
print("\nO valor total do salário líquido é R$",salario_liquido)

print("\n\n**************************")
print("*** SOBRE OS DESCONTOS ***")
print("**************************")
print("\nDesconto para aposentadoria: R$",desconto_aposentadoria)
print("\nDesconto para imposto de renda: R$",desconto_imposto_renda,"\n\n")
