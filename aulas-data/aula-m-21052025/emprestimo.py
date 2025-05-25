inadimplentes = ["João Silva", "Maria Souza", "Carlos Pereira"]

def verificar_emprestimo(nome, idade, renda):
    if nome in inadimplentes:
        return "inadimplente"
    if idade < 18 and renda < 2000:
        return "menor de idade e baixa renda"
    if idade < 18:
        return "menor de idade"
    if renda < 2000:
        return "baixa renda"
    return "elegível"