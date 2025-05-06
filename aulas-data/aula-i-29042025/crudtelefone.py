dicio = {
    "JUVENAL": "999888777",
    "PERITONIO": "666555444",
    "ESPATULA": "333222111",
    "MELANCIA": "222111000",
    "JULIENE":"111000999",
    "MELAO":"000999888",
    "ESTETOSCOPIO":"888777666",
    "BISTURI":"777666555",
    "LOGITECH":"666555444",
}

while True:
    print("\n********** MENU **********")
    print("1 - LISTAR")
    print("2 - CONSULTAR")
    print("3 - CADASTRAR")
    print("4 - ALTERAR")
    print("5 - DELETAR")
    print("0 - SAIR")
    opcao = input("ESCOLHA UMA OPÇÃO: ")

    if opcao == "1":
        print("\nLISTA DE REGISTROS")
        for nome in dicio:
            print(nome, "\t", dicio[nome])
    if opcao == "2":
        print("\nCONSULTAR")
        nomeprocurado = input("DIGITE O NOME A SER PROCURADO: ")
        if nomeprocurado in dicio:
            print(nomeprocurado, "\t", dicio[nomeprocurado])
        else:
            print("NOME NÃO ENCONTRADO!")
    if opcao == "3":
        print("\nCADASTRAR")
        nome = input("DIGITE O NOME: ")
        celular = input("DIGITE O CELULAR: ")
        dicio[nome] = celular
        print("REGISTRO CADASTRADO COM SUCESSO!")
    if opcao == "4":
        print("\nALTERAR")
        nomeprocurado = input("DIGITE O NOME A SER ALTERADO: ")
        if nomeprocurado in dicio:
            print("DADOS ATUAIS:")
            print("NOME: ", nomeprocurado)
            print("CELULAR: ", dicio[nomeprocurado])
            celular = input("DIGITE O NOVO CELULAR: ")
            dicio[nomeprocurado] = celular
            print("REGISTRO ALTERADO COM SUCESSO!")
        else:
            print("NOME NÃO ENCONTRADO!")
    if opcao == "5":
        print("\nDELETAR")
        nomeprocurado = input("DIGITE O NOME A SER DELETADO: ")
        if nomeprocurado in dicio:
            print("DADOS ENCONTRADOS:")
            print("NOME: ", nomeprocurado)
            print("CELULAR: ", dicio[nomeprocurado])
            del dicio[nomeprocurado]
            print("REGISTRO DELETADO COM SUCESSO!")
        else:
            print("NOME NÃO ENCONTRADO!")
    if opcao == "0":
        print("SAINDO DO SISTEMA...")
        break
    if opcao not in ["1", "2", "3", "4", "5", "0"]:
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
