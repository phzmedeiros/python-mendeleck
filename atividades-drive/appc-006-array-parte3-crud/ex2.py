dados=[ 
    ["001","PARAFUSO",120,40,0.50,18.0],
    ["002","BUCHA",80,20,0.30,18.0],
    ["003","BROCA",60,10,2.75,12.0]
]

while(True):
    print("\nSISTEMA ROMA - CONTROLE DE ESTOQUE")
    print("1 - LISTAR PRODUTOS")
    print("2 - CADASTRAR PRODUTO")
    print("3 - CONSULTAR POR ID")
    print("4 - CONSULTAR POR NOME")
    print("5 - DELETAR POR ID")
    print("6 - ALTERAR PRODUTO POR ID")
    print("\n0 - SAIR")
    opcao=input("\nDIGITE A SUA OPCAO: ")

    if(opcao=="0"):
        break

    if(opcao=="1"):
        print("\nLISTA DE PRODUTOS:")
        for vl in dados:
            print(vl)

    if(opcao=="2"):
        print("\nCADASTRAR PRODUTO:")
        idprod=input("DIGITE O ID DO PRODUTO: ")
        nome=input("DIGITE O NOME DO PRODUTO: ")
        qtd=int(input("DIGITE A QTD EM ESTOQUE: "))
        vendida=int(input("DIGITE A QTD VENDIDA: "))
        preco=float(input("DIGITE O PRECO UNITARIO: "))
        imposto=float(input("DIGITE O % DE ICMS: "))

        aux=[idprod,nome,qtd,vendida,preco,imposto]
        dados.append(aux)
        print("PRODUTO CADASTRADO.")

    if(opcao=="3"):
        print("\nCONSULTAR POR ID:")
        idBusca=input("DIGITE O ID: ")
        chave=0
        for vl in dados:
            if(idBusca==vl[0]):
                print("DADOS ENCONTRADOS:")
                print("ID:        ",vl[0])
                print("NOME:      ",vl[1])
                print("QTD ESTOQ: ",vl[2])
                print("QTD VENDID:",vl[3])
                print("PRECO:     ",vl[4])
                print("ICMS:      ",vl[5])
                chave=1
        if(chave==0):
            print("ID NAO CADASTRADO.")

    if(opcao=="4"):
        print("\nCONSULTAR POR NOME:")
        nomeBusca=input("DIGITE O NOME: ")
        chave=0
        for vl in dados:
            if(nomeBusca==vl[1]):
                print("DADOS ENCONTRADOS:")
                print("ID:        ",vl[0])
                print("NOME:      ",vl[1])
                print("QTD ESTOQ: ",vl[2])
                print("QTD VENDID:",vl[3])
                print("PRECO:     ",vl[4])
                print("ICMS:      ",vl[5])
                chave=1
        if(chave==0):
            print("NOME NAO CADASTRADO.")

    if(opcao=="5"):
        print("\nDELETAR PRODUTO POR ID:")
        idBusca=input("DIGITE O ID: ")
        chave=0
        for vl in dados:
            if(idBusca==vl[0]):
                dados.remove(vl)
                print("PRODUTO REMOVIDO.")
                chave=1
                break
        if(chave==0):
            print("ID NAO CADASTRADO.")

    if(opcao=="6"):
        print("\nALTERAR PRODUTO POR ID:")
        idBusca=input("DIGITE O ID: ")
        chave=0
        for pos,vl in enumerate(dados):
            if(idBusca==vl[0]):
                print("DADOS ATUAIS:")
                print("ID:        ",vl[0])
                print("NOME:      ",vl[1])
                print("QTD ESTOQ: ",vl[2])
                print("QTD VENDID:",vl[3])
                print("PRECO:     ",vl[4])
                print("ICMS:      ",vl[5])

                novoNome=input("NOVO NOME: ")
                novaQtd=input("NOVA QTD ESTOQUE: ")
                novaVend=input("NOVA QTD VENDIDA: ")
                novoPreco=input("NOVO PRECO: ")
                novoICMS=input("NOVO ICMS: ")

                if(novoNome!=""):
                    vl[1]=novoNome
                if(novaQtd!=""):
                    vl[2]=int(novaQtd)
                if(novaVend!=""):
                    vl[3]=int(novaVend)
                if(novoPreco!=""):
                    vl[4]=float(novoPreco)
                if(novoICMS!=""):
                    vl[5]=float(novoICMS)

                dados[pos]=vl
                print("DADOS ALTERADOS.")
                chave=1
        if(chave==0):
            print("ID NAO CADASTRADO.")
