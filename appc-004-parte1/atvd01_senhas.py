# TITULO DO PROGRAMA
print("************************************")
print("***SISTEMA DE LOGIN RAPIDOPOLENSE***")
print("************************************")

# DEFINIÇÃO DA SENHA
senha = "123321"

# ENTRADA DA TENTATIVA DO USUARIO
tentativa = input("\nDigite a senha => ")

# CONDICIONAL PARA VERIFICAÇÃO DA SENHA E LIBERAÇÃO DE ACESSO E RESPOSTA DO PROGRAMA
print("\n*********************")
if (tentativa == senha):
    print("** ACESSO PERMITIDO **")
if (tentativa != senha):
    print("*** ACESSO NEGADO ***")
print("*********************")