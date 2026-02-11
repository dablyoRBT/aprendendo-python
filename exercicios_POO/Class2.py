#Estado e comportamento

"""

Objetos possuem:
Estado -> Atributos
Comportamento -> Métodos/funções

"""

#Exemplo
class Lampada:
    def __init__(self):
        self.ligada = True

    def botao(self):
        self.ligada = not self.ligada

#Desafio 2
class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.velocidade = 0

    def acelerar(self, velocidade):
        print("Acelerando...")
        kmh = 0
        while kmh < velocidade:
            print(f"{kmh}km/h...")
            kmh += 10
            continue
        print(f"{velocidade}km/h...")
        self.velocidade = velocidade
        return self.velocidade
    
    def frear(self, velocidade):
        print("Freando...")
        velocidade_atual = velocidade
        while velocidade_atual > 0:
            print(f"{velocidade_atual}km/h...")
            velocidade_atual -= 5
            continue
        print("0km/h...")
        self.velocidade = 0

car = Carro("Fusca")
print(f"Velocidade: {car.velocidade}km/h")

velocidade = car.acelerar(50)
car.frear(velocidade)