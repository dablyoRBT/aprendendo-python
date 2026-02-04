#Calculando a gorjeta em um restaurante
def calcular_gorjeta(valor, porcentagem):
    gorjeta = valor * (porcentagem / 100)
    return gorjeta


#main
valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: "))

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print(f"Valor da gorjeta: R${gorjeta:.2f}")
print(f"Valor total a pagar: R${valor_conta + gorjeta:.2f}")
# =========================