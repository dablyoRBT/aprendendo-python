#Contando vogais de um txt

def contar_vogais(txt):
    vogais = "aeiou"
    contar_vogais = 0
    for char in txt.lower():
        if char in vogais:
            contar_vogais += 1
    return contar_vogais

#main
txt = input("Digite um texto: ")
print(f"O texto contém {contar_vogais(txt)} vogais.")