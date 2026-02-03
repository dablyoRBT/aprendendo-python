soma = lambda x, y: x + y 

subtrai = lambda x, y: x - y 

multiplica = lambda x, y: x * y 

divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

x = float(input("Digite o primeiro número: ")) 

y = float(input("Digite o segundo número: ")) 

operacao = input("Escolha a operação (| + | - | * | / |): ") 

match operacao:
    case "+":
        print(f"{x} + {y} = {soma(x, y)}")
    case "-":
        print(f"{x} - {y} = {subtrai(x, y)}")
    case "*":
        print(f"{x} * {y} = {multiplica(x, y)}")
    case "/":
        resultado = divide(x, y)
        print(f"{x} / {y} = {resultado}")
    case _:
        print("Operação inválida.")
