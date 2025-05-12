dados=[ 
    ["ADAMASTOR",63,"M",1.75,90.0,"120/80","O","SIM"],
    ["LINDOMARIO",71,"M",1.45,65.0,"130/85","A","NAO"],
    ["JUVENTINA",90,"F",1.45,70.0,"140/90","AB","SIM"]
]

while(True):
    print("\nSISTEMA CECAR - CENTRO CARDIOLOGICO")
    print("1 - LISTAR PACIENTES")
    print("2 - CADASTRAR PACIENTE")
    print("3 - CONSULTAR POR NOME")
    print("4 - DELETAR POR NOME")
    print("5 - ALTERAR DADOS POR NOME")
    print("\n0 - SAIR")
    opcao=input("\nDIGITE A SUA OPCAO: ")

    if(opcao=="0"):
        break

    if(opcao=="1"):
        print("\nLISTA DE PACIENTES:")
        for vl in dados:
            print(vl)

    if(opcao=="2"):
        print("\nCADASTRAR PACIENTE:")
        nome=input("DIGITE O NOME: ")
        idade=int(input("DIGITE A IDADE: "))
        sexo=input("DIGITE O SEXO (M/F): ")
        altura=float(input("DIGITE A ALTURA: "))
        peso=float(input("DIGITE O PESO: "))
        pressao=input("DIGITE A PRESSAO ARTERIAL: ")
        tipo=input("DIGITE O TIPO SANGUINEO (A, B, AB, O): ")
        comorbidade=input("COMORBIDADE CARDIACA (SIM/NAO): ")

        aux=[nome,idade,sexo,altura,peso,pressao,tipo,comorbidade]
        dados.append(aux)
        print("PACIENTE CADASTRADO.")

    if(opcao=="3"):
        print("\nCONSULTAR PACIENTE:")
        nomeProcurado=input("DIGITE O NOME: ")
        chaveProcura=0
        for vl in dados:
            if(nomeProcurado==vl[0]):
                print("DADOS ENCONTRADOS:")
                print("NOME:        ",vl[0])
                print("IDADE:       ",vl[1])
                print("SEXO:        ",vl[2])
                print("ALTURA:      ",vl[3])
                print("PESO:        ",vl[4])
                print("PRESSAO:     ",vl[5])
                print("TIPO SANGUE: ",vl[6])
                print("COMORBIDADE: ",vl[7])
                chaveProcura=1
        if(chaveProcura==0):
            print("NOME NAO CADASTRADO.")

    if(opcao=="4"):
        print("\nDELETAR PACIENTE:")
        nomeProcurado=input("DIGITE O NOME: ")
        chaveProcura=0
        for vl in dados:
            if(nomeProcurado==vl[0]):
                print("PACIENTE ENCONTRADO E REMOVIDO.")
                dados.remove(vl)
                chaveProcura=1
                break
        if(chaveProcura==0):
            print("NOME NAO CADASTRADO.")

    if(opcao=="5"):
        print("\nALTERAR DADOS DO PACIENTE:")
        nomeProcurado=input("DIGITE O NOME: ")
        chaveProcura=0
        for pos,vl in enumerate(dados):
            if(nomeProcurado==vl[0]):
                print("DADOS ATUAIS:")
                print("NOME:        ",vl[0])
                print("IDADE:       ",vl[1])
                print("SEXO:        ",vl[2])
                print("ALTURA:      ",vl[3])
                print("PESO:        ",vl[4])
                print("PRESSAO:     ",vl[5])
                print("TIPO SANGUE: ",vl[6])
                print("COMORBIDADE: ",vl[7])

                novoNome=input("NOVO NOME: ")
                novaIdade=input("NOVA IDADE: ")
                novoSexo=input("NOVO SEXO: ")
                novaAltura=input("NOVA ALTURA: ")
                novoPeso=input("NOVO PESO: ")
                novaPressao=input("NOVA PRESSAO: ")
                novoTipo=input("NOVO TIPO SANGUINEO: ")
                novaComorbidade=input("NOVA COMORBIDADE: ")

                if(novoNome!=""):
                    vl[0]=novoNome
                if(novaIdade!=""):
                    vl[1]=int(novaIdade)
                if(novoSexo!=""):
                    vl[2]=novoSexo
                if(novaAltura!=""):
                    vl[3]=float(novaAltura)
                if(novoPeso!=""):
                    vl[4]=float(novoPeso)
                if(novaPressao!=""):
                    vl[5]=novaPressao
                if(novoTipo!=""):
                    vl[6]=novoTipo
                if(novaComorbidade!=""):
                    vl[7]=novaComorbidade

                dados[pos]=vl
                print("DADOS ALTERADOS.")
                chaveProcura=1
        if(chaveProcura==0):
            print("NOME NAO CADASTRADO.")