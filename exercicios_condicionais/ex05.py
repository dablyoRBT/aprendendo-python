limite = 3000.0
despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > limite:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print(f"Você está dentro do orçamento. Você possui {3000 - despesas:.2f} de saldo restante até o limite.")