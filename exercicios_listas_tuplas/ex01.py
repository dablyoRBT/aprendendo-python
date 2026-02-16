despensa = ["Açucar", "Arroz", "Feijão", "Carne"]
carrinho = []

def verificar(compra):
    if compra in despensa:
        print(f"Você já possui {compra} na despensa.")
    else:
        carrinho.append(compra)
        print("Compra adicionada ao seu carrinho")

def estocar(carrinho):
    if carrinho:
        for item in carrinho:
            despensa.append(item)
            return despensa
    else:
        return despensa
    

compra = input("Digite o item que você quer verificar: ")
verificar(compra)
print(f"Sua despensa atual possui: {estocar(carrinho)}")