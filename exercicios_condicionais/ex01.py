macas = int(input("Digite quantas maçãs foram vendidas: "))
bananas = int(input("Digite quantas bananas foram vendidas: "))

if bananas > macas:
    print("Mais bananas foram vendidas do que maçãs.")
elif macas > bananas:
    print("Mais maçãs foram vendidas do que bananas.")
else:
    print("A quantidade de maçãs e bananas vendidas é igual.")