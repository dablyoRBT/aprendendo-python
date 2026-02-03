produtos = input("Digite os produtos separados por vírgula: ").split(",")
precos = input("Digite os preços separados por vírgula: ").split(",")

def vincular(produtos, precos):
    dicionario = {}
    i = 0
    for i in range(len(produtos)):
        dicionario[produtos[i]] = float(precos[i])
        print(f"Produto: {produtos[i]} | Preço: R$ {precos[i]}")
        i += 1

vincular(produtos, precos)