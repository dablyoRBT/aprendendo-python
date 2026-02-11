#Encapsulamento (Proteção de dados)

"""

Em Class do Python "_" ou "__":
_atributo -> protegido(convenção)...
__atributo -> privado(name mangling)

"""

#Controlando com @Property

class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.__saldo = saldo
    
    def __str__(self):
        return f"Cliente: {self.cliente}, Saldo: {self.saldo}"

    @property #Manipulando a maneira como um dado é visualizado
    def saldo(self):
        return self.__saldo - 10

    
#Desafio 3 
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, deposito):
        deposito = float(deposito)
        if deposito <= 0:
            print("Deposito inválido")
        else:
            self.__saldo = float(self.__saldo) + deposito

    def sacar(self, saque):
        saque = float(saque)
        if saque > self.__saldo:
            print("Valor de saque indisponivel")
        else:
            self.__saldo = float(self.__saldo) - saque

    def __str__(self):
        return f"Cliente: {self.titular}, Saldo: R$ {self.saldo}"

    @property
    def saldo(self):
        return round(float(self.__saldo), 2)

client1 = ContaBancaria("Dablyo", "1000.5")
client2 = ContaBancaria("Jose", 300)

client1.depositar("150")
client1.sacar("50") 

print(client1)