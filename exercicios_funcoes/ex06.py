lista = input("Digite os números separados por espaço: ").split()

def listar_pares(lista):
    pares = []
    for num in lista:
        if int(num) % 2 == 0:
            pares.append(int(num))
    return pares

print(f"Números pares: {listar_pares(lista)}")