# TITULO DO PROGRAMA
print("**************************************************")
print("*************CALCULADORA DE AZULEJOS**************")
print("**************************************************")

# ENTRADA DE DADOS - COMPRIMENTO E LARGURA DA SALA
comprimento_sala = float(input("\nDigite o comprimento da sala em metros: "))
largura_sala = float(input("Digite a largura da sala em metros: "))

# ENTRADA DE DADOS - COMPRIMENTO E LARGURA DO AZULEJO
comprimento_azulejo = float(input("\nDigite o comprimento do azulejo em centimetros: "))
largura_azulejo = float(input("Digite a largura do azulejo em centimetros: "))

# CALCULO DA AREA DA SALA E DO AZULEJO
area_sala = (comprimento_sala * 100) * (largura_sala * 100)
area_azulejo = comprimento_azulejo * largura_azulejo

# CALCULO DA QUANTIDADE DE AZULEJOS NECESSARIA
quantidade_azulejos = area_sala / area_azulejo

# TITULO DA SAIDA DE DADOS
print("\n\n**************************************************")
print("*************RESULTADO DO CALCULO*****************")
print("**************************************************")

# SAIDA DE DADOS - QUANTIDADE DE AZULEJOS NECESSARIA
print("\nA quantidade de azulejos necessaria para cobrir a sala é: ", quantidade_azulejos,"\n\n")
