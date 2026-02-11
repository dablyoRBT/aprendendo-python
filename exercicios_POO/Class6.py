#Polimorfismo: é a capacidade de um objeto se comportar de diferentes formas, dependendo do contexto em que é utilizado. Em Python, isso é alcançado por meio de métodos que podem ser sobrescritos em classes filhas.

#Desafio 5
class Funcionario:
    lsita = []
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Funcionario.lsita.append(self)

    def calcular_bonus(self):
        pass

    #Polimorfismo:
    @classmethod
    def printar_bonus(cls):
        for funcionario in cls.lsita:
            print(f"Bonus do/a {funcionario.nome}: R$ {funcionario.calcular_bonus()}")


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.2
    
class Vendedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.1
    
class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05

gerente = Gerente("Maria", 5000)
vendedor = Vendedor("João", 2500)
estagiario = Estagiario("Ana", 1500)

Funcionario.printar_bonus()