lista = ["A","A","A","R","R","A","A","A","S","S","S"]

aprovados = 0
reprovados = 0
substitutiva = 0

i = 0
while i < len(lista):
    if lista[i] == "A":
        aprovados = aprovados + 1
    elif lista[i] == "R":
        reprovados = reprovados + 1
    elif lista[i] == "S":
        substitutiva = substitutiva + 1
    i = i + 1

print("Alunos aprovados: ",aprovados)
print("Alunos reprovados: ",reprovados)
print("Alunos em substitutiva: ",substitutiva)