#Fundamentos

"""

O que é uma Class?
Class = molde
Objeto = instância do molde

EX:
Class ->  PessoaFisica
Objeto -> LUIS, CPF..., IDADE...

"""

#Estrutura base
class PessoaFisica:
    def __init__(self, nome, idade, cpf):
        self.nome = nome #atributo nome
        self.idade = idade #atributo idade
        self.cpf = cpf #atributo cpf
    
    #Metodo para objeto/self
    def metodo(self):
        pass

#Conceitos
"""

__init__ -> Construtor
self -> Próprio objeto
self.x -> Atributo do objeto
métodos -> Funções da class

"""

#Desafio 1
class Produto: 
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        print(self.nome)
        print(self.preco)

p1 = Produto("Maça", 4.99)
p1.exibir_info()
