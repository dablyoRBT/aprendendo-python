#Jogando pedra papel e tesoura com o computador
import random

def jogar_pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)
    return escolha_computador

#main
escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
escolha_computador = jogar_pedra_papel_tesoura()
if escolha_usuario not in ["pedra", "papel", "tesoura"]:
    print("Escolha inválida! Tente novamente.")
elif escolha_usuario == escolha_computador:
    print(f"Computador escolheu {escolha_computador}")
    print("Empate!")
elif ( 
    (escolha_usuario == "pedra" and escolha_computador == "tesoura") or 
    (escolha_usuario == "papel" and escolha_computador == "pedra") or 
    (escolha_usuario == "tesoura" and escolha_computador == "papel") 
): 
    print(f"Computador escolheu {escolha_computador}")
    print("Você venceu!") 
else:
    print(f"Computador escolheu {escolha_computador}")
    print("Computador venceu!")