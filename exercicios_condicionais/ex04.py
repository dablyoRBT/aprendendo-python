peso = float(input("Digite o peso da pessoa em kg: "))
altura = float(input("Digite a altura da pessoa em metros: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
else:
    print("Sobrepeso")