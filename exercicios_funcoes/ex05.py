valores = input("Digite os valores das vendas:")


def calcular_total_vendas(valores):
    valores = valores.split(" ")
    soma = 0
    for valor in valores:
        soma += float(valor)
    return soma

print(f"O total das vendas é R$ {calcular_total_vendas(valores)}")

