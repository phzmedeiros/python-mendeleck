dados = [ 
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
    print("7 - ATUALIZAR QTD VENDIDA POR ID")
    print("8 - CALCULAR PRECO COM IMPOSTO POR ID")
    print("9 - RELATÓRIOS")
    print("\n0 - SAIR")
    opcao = input("\nDIGITE A SUA OPÇÃO: ")

    if(opcao == "0"):
        break

    if(opcao == "1"):
        print("\nLISTA DE PRODUTOS:")
        for vl in dados:
            print(vl)

    if(opcao == "2"):
        print("\nCADASTRAR PRODUTO:")
        idprod = input("DIGITE O ID DO PRODUTO: ")
        nome = input("DIGITE O NOME DO PRODUTO: ")
        qtd = int(input("DIGITE A QTD EM ESTOQUE: "))
        vendida = int(input("DIGITE A QTD VENDIDA: "))
        preco = float(input("DIGITE O PRECO UNITARIO: "))
        imposto = float(input("DIGITE O % DE ICMS: "))
        aux = [idprod, nome, qtd, vendida, preco, imposto]
        dados.append(aux)
        print("PRODUTO CADASTRADO.")

    if(opcao == "3"):
        print("\nCONSULTAR POR ID:")
        idBusca = input("DIGITE O ID: ")
        chave = 0
        for vl in dados:
            if(idBusca == vl[0]):
                print("DADOS ENCONTRADOS:")
                print("ID:        ", vl[0])
                print("NOME:      ", vl[1])
                print("QTD ESTOQ: ", vl[2])
                print("QTD VENDID:", vl[3])
                print("PRECO:     ", vl[4])
                print("ICMS:      ", vl[5])
                chave = 1
        if(chave == 0):
            print("ID NAO CADASTRADO.")

    if(opcao == "4"):
        print("\nCONSULTAR POR NOME:")
        nomeBusca = input("DIGITE O NOME: ")
        chave = 0
        for vl in dados:
            if(nomeBusca == vl[1]):
                print("DADOS ENCONTRADOS:")
                print("ID:        ", vl[0])
                print("NOME:      ", vl[1])
                print("QTD ESTOQ: ", vl[2])
                print("QTD VENDID:", vl[3])
                print("PRECO:     ", vl[4])
                print("ICMS:      ", vl[5])
                chave = 1
        if(chave == 0):
            print("NOME NAO CADASTRADO.")

    if(opcao == "5"):
        print("\nDELETAR PRODUTO POR ID:")
        idBusca = input("DIGITE O ID: ")
        chave = 0
        for vl in dados:
            if(idBusca == vl[0]):
                dados.remove(vl)
                print("PRODUTO REMOVIDO.")
                chave = 1
                break
        if(chave == 0):
            print("ID NAO CADASTRADO.")

    if(opcao == "6"):
        print("\nALTERAR PRODUTO POR ID:")
        idBusca = input("DIGITE O ID: ")
        chave = 0
        for pos, vl in enumerate(dados):
            if(idBusca == vl[0]):
                print("DADOS ATUAIS:")
                print("ID:        ", vl[0])
                print("NOME:      ", vl[1])
                print("QTD ESTOQ: ", vl[2])
                print("QTD VENDID:", vl[3])
                print("PRECO:     ", vl[4])
                print("ICMS:      ", vl[5])
                novoNome = input("NOVO NOME: ")
                novaQtd = input("NOVA QTD ESTOQUE: ")
                novaVend = input("NOVA QTD VENDIDA: ")
                novoPreco = input("NOVO PRECO: ")
                novoICMS = input("NOVO ICMS: ")
                if(novoNome != ""):
                    vl[1] = novoNome
                if(novaQtd != ""):
                    vl[2] = int(novaQtd)
                if(novaVend != ""):
                    vl[3] = int(novaVend)
                if(novoPreco != ""):
                    vl[4] = float(novoPreco)
                if(novoICMS != ""):
                    vl[5] = float(novoICMS)
                dados[pos] = vl
                print("DADOS ALTERADOS.")
                chave = 1
        if(chave == 0):
            print("ID NAO CADASTRADO.")

    if(opcao == "7"):
        print("\nATUALIZAR QTD VENDIDA:")
        idBusca = input("DIGITE O ID: ")
        chave = 0
        for pos, vl in enumerate(dados):
            if(idBusca == vl[0]):
                novaVendida = int(input("NOVA QTD VENDIDA: "))
                vl[3] = novaVendida
                dados[pos] = vl
                print("QTD VENDIDA ATUALIZADA.")
                chave = 1
        if(chave == 0):
            print("ID NAO CADASTRADO.")

    if(opcao == "8"):
        print("\nCALCULAR PRECO COM IMPOSTO:")
        idBusca = input("DIGITE O ID: ")
        chave = 0
        for vl in dados:
            if(idBusca == vl[0]):
                preco = vl[4]
                imposto = vl[5]
                final = preco + (preco * imposto / 100)
                print("PRECO FINAL COM IMPOSTO: R$", round(final, 2))
                chave = 1
        if(chave == 0):
            print("ID NAO CADASTRADO.")

    if(opcao == "9"):
        print("\nRELATÓRIOS DISPONÍVEIS:")
        print("1 - CUSTO TOTAL POR PRODUTO")
        print("2 - VENDAS POR PRODUTO")
        print("3 - CUSTO TOTAL NO ESTOQUE")
        print("4 - VENDAS TOTAIS DO SISTEMA")
        print("5 - PRODUTOS ORDENADOS POR QTD VENDIDA (DECRESCENTE)")
        print("6 - PRODUTOS ORDENADOS POR VALOR TOTAL DE VENDA (DECRESCENTE)")
        subopcao = input("\nDIGITE A OPÇÃO DO RELATÓRIO: ")

        if(subopcao == "1"):
            print("\nRELATÓRIO: CUSTO TOTAL POR PRODUTO")
            for vl in dados:
                nome = vl[1]
                qtd = vl[2]
                preco = vl[4]
                custo = qtd * preco
                print("PRODUTO:", nome, "| CUSTO TOTAL ESTOQUE: R$", round(custo, 2))

        if(subopcao == "2"):
            print("\nRELATÓRIO: VENDAS POR PRODUTO")
            for vl in dados:
                nome = vl[1]
                qtdVendida = vl[3]
                preco = vl[4]
                totalVenda = qtdVendida * preco
                print("PRODUTO:", nome, "| QTD VENDIDA:", qtdVendida, "| VALOR: R$", round(totalVenda, 2))

        if(subopcao == "3"):
            print("\nRELATÓRIO: CUSTO TOTAL NO ESTOQUE")
            total = 0
            for vl in dados:
                total += vl[2] * vl[4]
            print("CUSTO TOTAL DO ESTOQUE: R$", round(total, 2))

        if(subopcao == "4"):
            print("\nRELATÓRIO: VENDAS TOTAIS")
            total = 0
            for vl in dados:
                total += vl[3] * vl[4]
            print("TOTAL VENDAS NO SISTEMA: R$", round(total, 2))

        if(subopcao == "5"):
            print("\nRELATÓRIO: ORDEM DECRESCENTE - QTD VENDIDA")
            ordenado = sorted(dados, key=lambda x: x[3], reverse=True)
            for vl in ordenado:
                print("PRODUTO:", vl[1], "| QTD VENDIDA:", vl[3])

        if(subopcao == "6"):
            print("\nRELATÓRIO: ORDEM DECRESCENTE - VALOR TOTAL DE VENDA")
            ordenado = sorted(dados, key=lambda x: x[3]*x[4], reverse=True)
            for vl in ordenado:
                valor = vl[3] * vl[4]
                print("PRODUTO:", vl[1], "| VALOR TOTAL DE VENDA: R$", round(valor, 2))