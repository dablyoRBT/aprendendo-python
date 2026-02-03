km = float(input("Digite a distância percorrida em quilômetros: "))

if km <= 100:
    print(f"Valor do pedágio: R$ {10.00}")
elif 100 <= km <= 200:
    print(f"Valor do pedágio: R$ {20.00}")
else:
    print(f"Valor do pedágio: R$ {30.00}")