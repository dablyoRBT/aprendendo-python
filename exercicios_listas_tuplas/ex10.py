#Desafio

despensa = ["Açucar", "Arroz", "Feijão", "Carne"]
carrinho = []

def verificar(compra):
    if compra in despensa:
        return True
    else:
        carrinho.append(compra)
        return False

def estocar(carrinho):
    if carrinho:
        for item in carrinho:
            despensa.append(item)
    return despensa

#Main
def main():
    while True:
        compra = input("Digite o item que você quer verificar (ou 'sair' para finalizar compras): ")
        if compra.lower() == 'sair':
            print(f"Encerrando programa...")
            break
        confirmacao = verificar(compra)
        if confirmacao:
            print(f"Você já possui {compra} na despensa.")
            continue
        else:
            print(f"{compra} adicionado ao carrinho de compras.")
            continue
    print(f"Lista atual de itens na despensa: {estocar(carrinho)}")

main()