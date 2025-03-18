# Título de entrada
print("*********************************")
print("**SISTEMA ACADEMICO DE HOGWARTS**")
print("*********************************")

# Leitura das notas e frequência
nota1 = float(input("Digite a nota da Avaliação 1: "))
nota2 = float(input("Digite a nota da Avaliação 2: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

# Calculando a média
media = (nota1 + nota2) / 2

# Verificando o status acadêmico
if frequencia < 75:
    status_frequencia = "Reprovado"
    status_academico = "Reprovado"
elif frequencia >= 75:
    if media <= 4.0:
        status_frequencia = "Aprovado"
        status_academico = "Reprovado"
    elif media > 4.0 and media <= 6.0:
        status_academico = "Exame"
        status_frequencia = "Aprovado"
    elif media > 6.0 and media <= 10.0:
        status_academico = "Aprovado"
        status_frequencia = "Aprovado"

# Título de saída
print("********************")
print("**BOLETIM DO ALUNO**")
print("********************")
print("Nota 1: ",nota1)
print("Nota 2: ",nota2)
print("Média: ",media)
print("Frequência: ",frequencia,"%")
print("Status de Frequência: ",status_frequencia)
print("Status Acadêmico: ",status_academico)
