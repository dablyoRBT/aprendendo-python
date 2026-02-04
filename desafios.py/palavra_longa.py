#Identificando palavras mais longas em um texto

def palavras_longas(txt):
    palavras = txt.split(" ")
    longas = list(filter(lambda palavra: len(palavra) >= 10, palavras))
    return longas

#main
txt = input("Digite um texto: ")
longas = palavras_longas(txt)
if not longas:
    print("Nenhuma palavra longa foi encontrada no texto.")
else:
    print("Palavras longas encontradas: ")
    for palavra in longas: 
        print(palavra)







