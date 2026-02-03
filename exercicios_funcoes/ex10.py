def soma_iterativa(n):
    total = 0
    for i in range(1, n + 1):
        total += i 
    return total

numero = int(input("Digite um número: "))
print(f"Resultado: {soma_iterativa(numero)}")