#Classe abstrata e método abstrato. Serve como um modelo para outras classes, garantindo que elas implementem certos métodos. Uma classe abstrata não pode ser INSTANCIADA diretamente, e um método abstrato é um método declarado na classe abstrata que deve ser implementado OBRIGATORIAMENTE pelas subclasses.

from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def processar(self):
        pass


class Cartao(Pagamento):
    def processar(self):
        print("Pagamento feito com cartão")


class Pix(Pagamento):
    def processar(self):
        print("Pagamento feito com Pix")

p1 = Cartao()
p2 = Pix()

p1.processar()
p2.processar()

#Desafio 6
from abc import ABC


class Transacao(ABC):
    @abstractmethod
    def verificar(self ,valor):
        pass

class Entrada(Transacao):
    def verificar(self, valor):
        if valor < 0:
            return "Valor de entrada não pode ser negativo"
        else:
            return f"Transação de entrada no valor de R$ {valor:.2f}"
    
class Saida(Transacao):
    def verificar(self, valor):
        if valor > 0:
            return "Valor de saída não pode ser positivo"
        else:
            return f"Transação de saída no valor de R$ {valor:.2f}"
    
s1 = Saida()
e1 = Entrada()

print(s1.verificar(100))
print(e1.verificar(100))


        