print("*******************************************************")
print("** PESQUISA QUALIDADE DE VIDA - RIDS RAPIDÓPOLIS **")
print("*******************************************************")

# Inicializando variáveis
total_entrevistas = 0
soma_idades = 0
soma_pesos = 0

idade_maxima = 0
idade_minima = 999

peso_maximo = 0
peso_minimo = 9999

faz_exercicio = 0
nao_faz_exercicio = 0

continuar = "S"

# Coleta de dados dos entrevistados
while continuar == "S":
    print("\n--- Dados do Entrevistado ---")
    
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (kg): "))
    exercicio = input("Faz exercícios regularmente? (S/N): ").upper()

    total_entrevistas = total_entrevistas + 1
    soma_idades = soma_idades + idade
    soma_pesos = soma_pesos + peso

    # Verifica maior e menor idade
    if idade > idade_maxima:
        idade_maxima = idade
    if idade < idade_minima:
        idade_minima = idade

    # Verifica maior e menor peso
    if peso > peso_maximo:
        peso_maximo = peso
    if peso < peso_minimo:
        peso_minimo = peso

    # Contabiliza exercício
    if exercicio == "S":
        faz_exercicio = faz_exercicio + 1
    else:
        nao_faz_exercicio = nao_faz_exercicio + 1

    continuar = input("\nDeseja inserir outro entrevistado? (S/N): ").upper()

# Cálculos finais
media_idade = soma_idades / total_entrevistas
media_peso = soma_pesos / total_entrevistas
percentual_faz_exercicio = (faz_exercicio / total_entrevistas) * 100
percentual_nao_faz_exercicio = (nao_faz_exercicio / total_entrevistas) * 100

# Resultados finais
print("\n\n*******************************************************")
print("** RESULTADOS DA PESQUISA QUALIDADE DE VIDA **")
print("*******************************************************")

print(f"\nTotal de entrevistas realizadas: {total_entrevistas}")

print(f"\nIdade média: {media_idade:.2f} anos")
print(f"Idade máxima: {idade_maxima} anos")
print(f"Idade mínima: {idade_minima} anos")

print(f"\nPeso médio: {media_peso:.2f} kg")
print(f"Peso máximo: {peso_maximo:.2f} kg")
print(f"Peso mínimo: {peso_minimo:.2f} kg")

print(f"\nPessoas que fazem exercícios regularmente: {faz_exercicio} ({percentual_faz_exercicio:.2f}%)")
print(f"Pessoas que NÃO fazem exercícios regularmente: {nao_faz_exercicio} ({percentual_nao_faz_exercicio:.2f}%)")
