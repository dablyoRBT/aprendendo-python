#Contando cédulas unicas no saque
def sacar(saque):
    cedulas = [100, 50, 20, 10, 5, 2]

    for nota in cedulas:
        if nota == 5:
            if saque >= 5 and (saque - 5) % 2 == 0:
                qtd = 1
            else:
                qtd = 0
        else:
            qtd = saque // nota

        if qtd > 0:
            print(f"{qtd} de {nota}")
            saque -= qtd * nota


#main
while True:
    try:
        saque = int(input("Digite o valor do saque: "))
        if saque % 2 > 0:
             print("Erro: O valor deve ser múltiplo de 2. Tente novamente.")
             continue
        else:
            sacar(saque)
            break
    except ValueError:
        print("Por favor digite um valor válido.")
        continue