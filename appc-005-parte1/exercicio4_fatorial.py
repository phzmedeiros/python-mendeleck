print("***********************")
print("**CÁLCULO DO FATORIAL**")
print("***********************")

# LEITURA DO NÚMERO
n = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1

# CÁLCULO DO FATORIAL
if n < 0:
    print("Fatorial não é definido para números negativos!")
else:
    i = 1
    while i <= n:
        fatorial = fatorial * i
        i = i + 1
    print(f"\n{n}! = {fatorial}")
    