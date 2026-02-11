#Métodos Especiais (DUNDER METHODS)

"""

__str__  -> Representação amigável.
__repr__ -> Representação técnica.

"""

#Exemplo
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    #Usado no terminal por devs
    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco})"
    
    #Ou

    #Padrao para o usuário final
    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
    
p1 = Produto("Maça", 4.99)
print(p1)
