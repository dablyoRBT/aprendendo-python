#Adivinhando o numero secreto proposto pelo computador
import random

def sortear_numero_secreto():
    numero_secreto = random.randint(1, 100)
    return numero_secreto

#main
numero = sortear_numero_secreto()
print(f"\nBem-vindo ao jogo do número secreto!\n")
while True:
    try:
        tentativa = int(input("Digite um número entre 1 e 100 (ou 0 para sair): "))
        if tentativa > 100 or tentativa < 0:
            print("Número fora do intervalo! Tente novamente.")
            continue
        elif tentativa == 0:
            print(f"O número secreto era: {numero}. Até a próxima!")
            break
        elif tentativa < numero:
            print("Tente um número maior!")
            continue
        elif tentativa > numero:
            print("Tente um número menor!")
            continue
        else:
            print(f"Parabéns! O número secreto era {numero}. Você acertou!")
            break
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
        continue
    
