# TITULO DO PROGRAMA
print("*******************************************")
print("***SOFTWARE RAPIDOPOLENSE DE INTERLAGOAS***")
print("*******************************************")
print("**Um oferecimento de Taguy Reuerpidópolis**")
print("*******************************************")

# ENTRADA DE DADOS
print("\nPrimeiro trecho")
distancia_trecho_1 = float(input("Insira a distância percorrida no primeiro trecho em metros (m)= "))
tempo_trecho_1 = float(input("Insira o tempo de percurso do primeiro trecho em segundos (s)= "))
print("\nSegundo trecho")
distancia_trecho_2 = float(input("Insira a distância percorrida no segundo trecho em metros (m)= "))
tempo_trecho_2 = float(input("Insira o tempo de percurso do segundo trecho em segundos (s)= "))
print("\nTerceiro trecho")
distancia_trecho_3 = float(input("Insira a distância percorrida no terceiro trecho em metros (m)= "))
tempo_trecho_3 = float(input("Insira o tempo de percurso do terceiro trecho em segundos (s)= "))
print("\nQuarto trecho")
distancia_trecho_4 = float(input("Insira a distância percorrida no quarto trecho em metros (m)= "))
tempo_trecho_4 = float(input("Insira o tempo de percurso do quarto trecho em segundos (s)= "))

# CÁLCULO DA VELOCIDADE MÉDIA PARA CADA TRECHO
velocidade_media_trecho_1 = distancia_trecho_1 / tempo_trecho_1
velocidade_media_trecho_2 = distancia_trecho_2 / tempo_trecho_2
velocidade_media_trecho_3 = distancia_trecho_3 / tempo_trecho_3
velocidade_media_trecho_4 = distancia_trecho_4 / tempo_trecho_4

# CÁLCULO DA VELOCIDADE MÉDIA TOTAL
distancia_total = distancia_trecho_1 + distancia_trecho_2 + distancia_trecho_3 + distancia_trecho_4
tempo_total = tempo_trecho_1 + tempo_trecho_2 + tempo_trecho_3 + tempo_trecho_4
velocidade_media_total = distancia_total / tempo_total

# CÁLCULO DA ACELERAÇÃO ENTRE TRECHOS CONSECUTIVOS
aceleracao_1_2 = (velocidade_media_trecho_2 - velocidade_media_trecho_1) / tempo_trecho_2
aceleracao_2_3 = (velocidade_media_trecho_3 - velocidade_media_trecho_2) / tempo_trecho_3
aceleracao_3_4 = (velocidade_media_trecho_4 - velocidade_media_trecho_3) / tempo_trecho_4

# SAÍDA DE DADOS
print("\n\n**************************************************")
print("*********RESULTADO DO SOFTWARE INTERLAGOAS********")
print("**************************************************")
# SAÍDA DE VELOCIDADE MÉDIA
print("\nVELOCIDADES\n")
print(f"Velocidade média do trecho 1: {velocidade_media_trecho_1:.2f} m/s")
print(f"Velocidade média do trecho 2: {velocidade_media_trecho_2:.2f} m/s")
print(f"Velocidade média do trecho 3: {velocidade_media_trecho_3:.2f} m/s")
print(f"Velocidade média do trecho 4: {velocidade_media_trecho_4:.2f} m/s")
print(f"\nVelocidade média total: {velocidade_media_total:.2f} m/s")

# SAÍDA DE ACELERAÇÃO
print("\n\nACELERAÇÕES\n")
print(f"Aceleração entre o trecho 1 e 2: {aceleracao_1_2:.2f} m/s²")
print(f"Aceleração entre o trecho 2 e 3: {aceleracao_2_3:.2f} m/s²")
print(f"Aceleração entre o trecho 3 e 4: {aceleracao_3_4:.2f} m/s²\n\n")