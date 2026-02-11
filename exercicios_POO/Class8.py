#Composição

"""

Composição = uma classe usa outra classe. 

"""

#Exemplo
class Pedido:
    def __init__(self):
        self.produtos = []


#desafio 7
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return f"Total: R$ {total:.2f}"
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(f"{produto.nome} - R$ {produto.preco:.2f}")

    def remover_produto(self, removido):
        if removido in self.produtos:
            for produto in self.produtos:
                if removido == produto:
                    self.produtos.remove(produto)
                    print(f"O produto {removido.nome} foi removido do carrinho")
                else:
                    continue
        else:
            print("Esse produto não esta no carrinho")

    

carrinho = CarrinhoDeCompras()
p1 = Produto("Camisa", 50.0)
p2 = Produto("Calça", 100.0)
p3 = Produto("Tênis", 150.0)

carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)

carrinho.listar_produtos()

carrinho.remover_produto(p2)

print(carrinho.calcular_total())