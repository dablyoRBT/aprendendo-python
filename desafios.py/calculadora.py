#Calculadora simples com tratamento de erros
def calcular(value1, op, value2):
    match op:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "/":
            return value1 / value2

#main
operacoes = ("+", "-", "*", "/")
try:
    n1 = float(input("Digite o primeiro número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    if operacao not in operacoes:
        print("Operação invalida.")
    else:
        n2 = float(input("Digite o segundo número: "))  
        print(f"Resultado: {calcular(n1, operacao, n2)}")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
except ZeroDivisionError:
    print("Erro de divisão por zero. Um número não pode ser dividio por 0.")
    


