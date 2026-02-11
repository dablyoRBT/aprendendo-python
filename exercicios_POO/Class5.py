#Herança de classes

"""
A herança permite criar uma nova classe a partir de uma classe existente, herdando seus atributos e métodos. A classe existente é chamada de classe base ou superclasse, enquanto a nova classe é chamada de classe derivada ou subclasse. A subclasse pode adicionar novos atributos e métodos, ou modificar os existentes, para se adequar às suas necessidades específicas. Facilitando a reutilização de código e promovendo a hierarquia entre classes.
"""
class Animal:
    def diferenca(self):
        pass

    def falar(self):
        pass
    
    def mover(self, animal):
        return f"O {animal} se move"
    
    def cor(self, animal, cor):
        return f"O {animal} tem uma cor {cor}"

class Cachorro(Animal):
    def falar(self):
        return "Au au"
    
    def diferenca(self):
        return "O cachorro late"
    
class Gato(Animal):
    def falar(self):
        return "Miau"
    
    def diferenca(self):
        return "O gato mia"


#Desafio 4
class Funcionario:
    lsita = []
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Funcionario.lsita.append(self)

    def calcular_bonus(self):
        pass

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

print(f"Bonus do/a gerente {gerente.nome}: R$ {gerente.calcular_bonus()}")
print(f"Bonus do/a vendedor/a {vendedor.nome}: R$ {vendedor.calcular_bonus()}")
print(f"Bonus do/a estagiário/a {estagiario.nome}: R$ {estagiario.calcular_bonus()}")
