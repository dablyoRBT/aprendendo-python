# =========================
# Funções 
# =========================

def saudacao(usuario):
    print(f"Olá, {usuario}!") 
    

saudacao("Dablyo") # "Olá, Dablyo!"

# =========================
# Return
# =========================

def soma(a, b):
    return a + b

result = soma(4, 5)
print(result) # 9

# =========================
# Funções anonimas (lambda)
# =========================

quadrado = lambda x: x ** 2
print(quadrado(5)) # 25

# =========================
# Funções com varios valores variados
# =========================

def soma_variavel(*numeros): # Usamos o *(parâmetro) para permitir que nosso parâmetro trabalhe com multiplos valores
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # 6
print(soma_variavel(4, 5, 6, 7))  # 22

# =========================
# Uso de "Docstrings" -> """ txt """
# =========================

def saudacao(usuario):
    """
    Isso é uma docstring é uma boa prática documentar nossas funções
    
    :param usuario: recebe o valor/nome de quem vai receber a saudação
    """
    print(f"Olá, {usuario}!") 
    

saudacao("Dablyo") # "Olá, Dablyo!"