# CÁLCULO DA MÉDIA DE SATISFAÇÃO
print("\n*************************************************")
print("*** CÁLCULO DA MÉDIA DE SATISFAÇÃO DOS ALUNOS ***")
print("*************************************************")

# ENTRADA DE DADOS - NOTAS
nota_aluno_1 = float(input("\nDigite a nota do aluno 1 (0 a 10): "))
nota_aluno_2 = float(input("Digite a nota do aluno 2 (0 a 10): "))
nota_aluno_3 = float(input("Digite a nota do aluno 3 (0 a 10): "))
nota_aluno_4 = float(input("Digite a nota do aluno 4 (0 a 10): "))
nota_aluno_5 = float(input("Digite a nota do aluno 5 (0 a 10): "))

# CÁLCULO DA MÉDIA
media = (nota_aluno_1 + nota_aluno_2 + nota_aluno_3 + nota_aluno_4 + nota_aluno_5) / 5

# SAÍDA DE DADOS
print("\n\n***************************************************")
print("*** RESULTADO DO CÁLCULO DA MÉDIA DE SATISFAÇÃO ***")
print("***************************************************")
print(f"\nA média de satisfação dos alunos é: {media:.2f}\n\n")