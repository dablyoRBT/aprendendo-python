# =========================
# Erro de sintaxe (SyntaxError)
# =========================
'''
def minha_funcao() # Faltam os dois pontos
    print("Olá")
'''
# =========================
# Erro de nome (NameError)
# =========================
'''
print(variavel_nao_definida) # var indefinida
'''
# =========================
# Erro de tipo (TypeError)
# =========================
'''
resultado = 5 + "10" # Tipos incompatíveis value e string
'''
# =========================
# Erro de índice (IndexError)
# =========================
'''
lista = [1, 2, 3]
print(lista[3])  # O índice/index 3 está fora do intervalo
'''
# =========================
# Try, except e finally
# =========================

try: # Try contem o bloco de código que pode gerar uma exceção/error
    resultado = 10 / 0  # Divisão por zero "ZeroDivisionError"
    print(resultado)
except ZeroDivisionError: # Except() especifica o tipo de exceção que se deseja capturar e lidar "Preve e trata o erro"
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

# Ao usar finally ele sempre sera executado independente se houver erros ou não
try:
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção

