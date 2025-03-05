# TITULO DO PROGRAMA
print("**************************************************")
print("*************CALCULADORA DE AZULEJOS**************")
print("**************************************************")

# ENTRADA DE DADOS - COMPRIMENTO E LARGURA DA SALA
comprimentosala = float(input("\nDigite o comprimento da sala em metros: "))
largurasala = float(input("Digite a largura da sala em metros: "))

# ENTRADA DE DADOS - COMPRIMENTO E LARGURA DO AZULEJO
comprimentoazulejo = float(input("\nDigite o comprimento do azulejo em centimetros: "))
larguraazulejo = float(input("Digite a largura do azulejo em centimetros: "))

# CALCULO DA AREA DA SALA E DO AZULEJO
areasala = (comprimentosala * 100) * (largurasala * 100)
areaazulejo = comprimentoazulejo * larguraazulejo

# CALCULO DA QUANTIDADE DE AZULEJOS NECESSARIA
quantidadeazulejos = areasala / areaazulejo

# TITULO DA SAIDA DE DADOS
print("\n\n**************************************************")
print("*************RESULTADO DO CALCULO*****************")
print("**************************************************")

# SAIDA DE DADOS - QUANTIDADE DE AZULEJOS NECESSARIA
print("\nA quantidade de azulejos necessaria para cobrir a sala é: ", quantidadeazulejos)