dados = [ 
    ["ADAMASTOR",63,"M",1.75,90.0,"120/80","O","SIM"],
    ["LINDOMARIO",71,"M",1.45,65.0,"130/85","A","NAO"],
    ["JUVENTINA",90,"F",1.45,70.0,"140/90","AB","SIM"]
]

while(True):
    print("\nSISTEMA CECAR - CENTRO CARDIOLÓGICO")
    print("1 - LISTAR PACIENTES")
    print("2 - CADASTRAR PACIENTE")
    print("3 - CONSULTAR POR NOME")
    print("4 - DELETAR POR NOME")
    print("5 - ALTERAR DADOS POR NOME")
    print("6 - RELATÓRIOS")
    print("\n0 - SAIR")
    opcao = input("\nDIGITE A SUA OPÇÃO: ")

    if(opcao == "0"):
        break

    if(opcao == "1"):
        print("\nLISTA DE PACIENTES:")
        for vl in dados:
            print(vl)

    if(opcao == "2"):
        print("\nCADASTRAR PACIENTE:")
        nome = input("DIGITE O NOME: ")
        idade = int(input("DIGITE A IDADE: "))
        sexo = input("DIGITE O SEXO (M/F): ")
        altura = float(input("DIGITE A ALTURA: "))
        peso = float(input("DIGITE O PESO: "))
        pressao = input("DIGITE A PRESSÃO ARTERIAL: ")
        tipo = input("DIGITE O TIPO SANGUÍNEO (A, B, AB, O): ")
        comorbidade = input("COMORBIDADE CARDÍACA (SIM/NAO): ")

        aux = [nome, idade, sexo, altura, peso, pressao, tipo, comorbidade]
        dados.append(aux)
        print("PACIENTE CADASTRADO.")

    if(opcao == "3"):
        print("\nCONSULTAR PACIENTE:")
        nomeProcurado = input("DIGITE O NOME: ")
        chave = 0
        for vl in dados:
            if(nomeProcurado == vl[0]):
                print("DADOS ENCONTRADOS:")
                print("NOME:       ", vl[0])
                print("IDADE:      ", vl[1])
                print("SEXO:       ", vl[2])
                print("ALTURA:     ", vl[3])
                print("PESO:       ", vl[4])
                print("PRESSÃO:    ", vl[5])
                print("TIPO SANG.: ", vl[6])
                print("COMORBIDADE:", vl[7])
                chave = 1
        if(chave == 0):
            print("NOME NÃO CADASTRADO.")

    if(opcao == "4"):
        print("\nDELETAR PACIENTE:")
        nomeProcurado = input("DIGITE O NOME: ")
        chave = 0
        for vl in dados:
            if(nomeProcurado == vl[0]):
                dados.remove(vl)
                print("PACIENTE REMOVIDO.")
                chave = 1
                break
        if(chave == 0):
            print("NOME NÃO CADASTRADO.")

    if(opcao == "5"):
        print("\nALTERAR DADOS DO PACIENTE:")
        nomeProcurado = input("DIGITE O NOME: ")
        chave = 0
        for pos, vl in enumerate(dados):
            if(nomeProcurado == vl[0]):
                print("DADOS ATUAIS:")
                print("NOME:       ", vl[0])
                print("IDADE:      ", vl[1])
                print("SEXO:       ", vl[2])
                print("ALTURA:     ", vl[3])
                print("PESO:       ", vl[4])
                print("PRESSÃO:    ", vl[5])
                print("TIPO SANG.: ", vl[6])
                print("COMORBIDADE:", vl[7])

                novoNome = input("NOVO NOME: ")
                novaIdade = input("NOVA IDADE: ")
                novoSexo = input("NOVO SEXO: ")
                novaAltura = input("NOVA ALTURA: ")
                novoPeso = input("NOVO PESO: ")
                novaPressao = input("NOVA PRESSÃO: ")
                novoTipo = input("NOVO TIPO SANGUÍNEO: ")
                novaComorb = input("NOVA COMORBIDADE: ")

                if(novoNome != ""):
                    vl[0] = novoNome
                if(novaIdade != ""):
                    vl[1] = int(novaIdade)
                if(novoSexo != ""):
                    vl[2] = novoSexo
                if(novaAltura != ""):
                    vl[3] = float(novaAltura)
                if(novoPeso != ""):
                    vl[4] = float(novoPeso)
                if(novaPressao != ""):
                    vl[5] = novaPressao
                if(novoTipo != ""):
                    vl[6] = novoTipo
                if(novaComorb != ""):
                    vl[7] = novaComorb

                dados[pos] = vl
                print("DADOS ALTERADOS.")
                chave = 1
        if(chave == 0):
            print("NOME NÃO CADASTRADO.")

    if(opcao == "6"):
        print("\nRELATÓRIOS DISPONÍVEIS:")
        print("1 - PACIENTES POR SEXO")
        print("2 - COMORBIDADE POR SEXO")
        print("3 - COMORBIDADE POR FAIXA ETÁRIA")
        print("4 - LISTAR IMC DE TODOS OS PACIENTES")
        print("5 - PACIENTES POR TIPO SANGUÍNEO")
        print("6 - PACIENTES COM PRESSÃO ACIMA DE UM VALOR")
        sub = input("DIGITE A OPÇÃO: ")

        if(sub == "1"):
            masc = fem = 0
            for vl in dados:
                if(vl[2] == "M"):
                    masc += 1
                if(vl[2] == "F"):
                    fem += 1
            print("TOTAL MASCULINO:", masc)
            print("TOTAL FEMININO:", fem)

        if(sub == "2"):
            for sexo in ["M","F"]:
                total = comorb = 0
                for vl in dados:
                    if(vl[2]==sexo):
                        total += 1
                        if(vl[7] == "SIM"):
                            comorb += 1
                if total > 0:
                    sem = total - comorb
                    print(f"SEXO {sexo}: {comorb} COM COMORBIDADE ({round(comorb/total*100,1)}%) | {sem} SEM ({round(sem/total*100,1)}%)")

        if(sub == "3"):
            faixas = [(0,15),(16,30),(31,55),(56,999)]
            for faixa in faixas:
                ini,fim = faixa
                total = comorb = 0
                for vl in dados:
                    idade = vl[1]
                    if idade >= ini and idade <= fim:
                        total += 1
                        if(vl[7] == "SIM"):
                            comorb += 1
                if total > 0:
                    sem = total - comorb
                    print(f"{ini}-{fim} ANOS: {comorb} COM COMORBIDADE ({round(comorb/total*100,1)}%) | {sem} SEM ({round(sem/total*100,1)}%)")

        if(sub == "4"):
            for vl in dados:
                imc = vl[4] / (vl[3]**2)
                print("PACIENTE:", vl[0], "| IMC:", round(imc,2))

        if(sub == "5"):
            tipos = ["A","B","AB","O"]
            for tipo in tipos:
                cont = 0
                for vl in dados:
                    if(vl[6] == tipo):
                        cont += 1
                print("TIPO",tipo,"=",cont,"PACIENTES")

        if(sub == "6"):
            valor = input("DIGITE A PRESSÃO LIMITE (ex: 130): ")
            limite = int(valor)
            print("\nPACIENTES COM PRESSÃO MAIOR QUE", limite)
            for vl in dados:
                sistolica = int(vl[5].split("/")[0])
                if sistolica > limite:
                    print("PACIENTE:", vl[0], "| PRESSÃO:", vl[5])
