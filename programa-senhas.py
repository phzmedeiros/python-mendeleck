# DEFINIÇÃO DA SENHA
senha = "123321"

# TITULO DO PROGRAMA
print("************************************")
print("***SISTEMA DE LOGIN RAPIDOPOLENSE***")
print("************************************")

# ENTRADA DA TENTATIVA DO USUARIO
tentativa = input("\nDigite a senha = ")

# CONDICIONAL PARA VERIFICAÇÃO DA SENHA E LIBERAÇÃO DE ACESSO
print("\n\n*******************")
if (tentativa == senha):
    print("**ACESSO LIBERADO**")
if (tentativa != senha):
    print("***ACESSO NEGADO***")
print("*******************")
