data = [
    ["Pedro Henrique", 19, 1.73],
    ["Lucas", 20, 1.80],
    ["Mariana", 27, 1.65],
    ["Carlos", 32, 1.75],
    ["Fernanda", 29, 1.60],
    ["Ricardo", 31, 1.85],
    ["Patrícia", 26, 1.70],
    ["Gabriel", 24, 1.78],
    ["Juliana", 33, 1.68],
    ["Thiago", 21, 1.82],
    ["Larissa", 34, 1.64],
    ["Eduardo", 23, 1.77],
    ["Camila", 36, 1.66],
    ["André", 19, 1.79],
    ["Roberta", 38, 1.63],
    ["Felipe", 37, 1.81],
    ["Tatiane", 39, 1.67],
    ["Bruno", 40, 1.74],
    ["Aline", 41, 1.69],
    ["Rafael", 42, 1.76],
    ["Vanessa", 43, 1.72],
    ["Gustavo", 44, 1.78],
    ["Sabrina", 45, 1.71],
    ["Diego", 46, 1.80],
    ["Claudia", 47, 1.65],
    ["Leonardo", 48, 1.83],
    ["Juliana", 49, 1.70],
    ["Marcos", 50, 1.77],
    ["Ana", 51, 1.62],
    ["Robson", 52, 1.84],
    ["Juliana", 53, 1.66],
    ["Thiago", 54, 1.78],
    ["Larissa", 55, 1.69],
    ["Eduardo", 56, 1.75],
    ["Camila", 57, 1.68],
    ["André", 58, 1.80],
    ["Roberta", 59, 1.64],
    ["Felipe", 60, 1.82],
    ["Tatiane", 61, 1.67],
    ["Bruno", 62, 1.74],
    ["Aline", 63, 1.70],
    ["Rafael", 64, 1.76],
    ["Vanessa", 65, 1.72],
    ["Gustavo", 66, 1.78],
    ["Sabrina", 67, 1.71],
    ["Diego", 68, 1.80],
    ["Claudia", 69, 1.65],
    ["Leonardo", 70, 1.83],
    ["Juliana", 71, 1.70]   
]

while(True):
    print("\n********** SISTEMA **********")
    print("1 - CADASTRAR")
    print("2 - LISTAR")
    print("3 - CONSULTAR")
    print("4 - DELETAR")
    print("5 - ALTERAR")
    print("0 - SAIR")
    opcao = input("ESCOLHA UMA OPÇÃO: ")

    if(opcao == "1"):
        print("CADASTRAR")
        nome = input("DIGITE O NOME: ")
        idade = int(input("DIGITE A IDADE: "))
        altura = float(input("DIGITE A ALTURA (EM METROS): "))
        data.append([nome, idade, altura])
        print("REGISTRO CADASTRADO COM SUCESSO!")
    
    if(opcao == "2"):
        print("\n********** LISTA DE REGISTROS **********")
        for vl in data:
            nome = vl[0]
            idade = vl[1]
            altura = vl[2]
            print("NOME: ", nome)
            print("IDADE: ", idade)
            print("ALTURA: ", altura)
            print("---------------------------------------")
    
    if(opcao == "3"):
        print("CONSULTAR")
        nomeprocurado = input("DIGITE O NOME A SER PROCURADO: ")
        chaveprocura = 0
        for vl in data:
            nome = vl[0]
            if(nomeprocurado == nome):
                print("DADOS ENCONTRADOS")
                print("NOME: ", vl[0])
                print("IDADE: ", vl[1])
                print("ALTURA: ", vl[2])
                chaveprocura = 1
        if(chaveprocura == 0):
            print("NOME NÃO ENCONTRADO!")
    
    if(opcao == "4"):
        print("DELETAR")
        nomeprocurado = input("DIGITE O NOME A SER PROCURADO: ")
        chaveprocura = 0
        for vl in data:
            nome = vl[0]
            if(nomeprocurado == nome):
                print("DADOS ENCONTRADOS")
                print("NOME: ", vl[0])
                print("IDADE: ", vl[1])
                print("ALTURA: ", vl[2])
                data.remove(vl)
                print("REGISTRO DELETADO COM SUCESSO!")
                chaveprocura = 1
                break
        if(chaveprocura == 0):
            print("NOME NÃO ENCONTRADO!")
    
    if(opcao == "5"):
        print("ALTERAR")
        nomeprocurado = input("DIGITE O NOME A SER PROCURADO: ")
        chaveprocura = 0
        for vl in data:
            nome = vl[0]
            if(nomeprocurado == nome):
                print("DADOS ENCONTRADOS")
                print("NOME: ", vl[0])
                print("IDADE: ", vl[1])
                print("ALTURA: ", vl[2])
                vl[0] = input("DIGITE O NOVO NOME: ")
                vl[1] = int(input("DIGITE A NOVA IDADE: "))
                vl[2] = float(input("DIGITE A NOVA ALTURA (EM METROS): "))
                print("REGISTRO ALTERADO COM SUCESSO!")
                chaveprocura = 1
        if(chaveprocura == 0):
            print("NOME NÃO ENCONTRADO!")
    
    if(opcao == "0"):
        print("SAINDO DO SISTEMA...")
        break
    
    if(opcao not in ["1", "2", "3", "4", "5", "0"]):
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
