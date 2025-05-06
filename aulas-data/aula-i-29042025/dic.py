dicio = {
    "JUVENAL":"999888777",
    "PERITONIO":"666555444",
    "ESPATULA":"333222111",
}

for i in dicio:
    print(i)

for i in dicio:
    print(i,"\t",dicio[i])

print("CONSULTA AO DICIONARIO")
nomeprocurado = input("DIGITE O NOME A SER PROCURADO: ")
try:
    print(nomeprocurado,"\t",dicio[nomeprocurado])
except:
    print("NOME NAO CADASTRADO")

print("CADASTRAR")
nome = input("DIGITE O NOME A SER CADASTRADO: ")
celular = input("DIGITE O CELULAR A SER CADASTRADO: ")
