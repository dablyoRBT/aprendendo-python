# =========================
# LISTAS (mutáveis)
# =========================

frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")       # adiciona no final
frutas.insert(1, "uva")     # adiciona em um índice específico
frutas.remove("banana")     # remove pelo valor
fruta_removida = frutas.pop(2)  # remove pelo índice e retorna o valor na var fruta_removida
frutas.sort()    # ordena em ordem alfabética
frutas.reverse() # inverte a ordem


# =========================
# TUPLAS (imutáveis)
# =========================

minha_tupla = (1, 2, 3, 2, 4, 2)

print(minha_tupla[0])        # acesso por índice
print(len(minha_tupla))      # quantidade de elementos
print(minha_tupla.count(2))  # quantas vezes o valor aparece
print(minha_tupla.index(2))  # posição do valor 


# =========================
# DICIONÁRIOS (chave : valor)
# =========================

pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "Madri"
}

print(pessoa["nome"])  # acesso pelo nome da chave
print(pessoa.keys())    # retorna as chaves
print(pessoa.values())  # retorna os valores
print(pessoa.items())   # retorna chave e valor juntos
pessoa.update({"profissao": "Engenheiro"})  # adiciona novo campo


# =========================
# CONJUNTOS (sets) - valores únicos podem ser criados por Set() ou {}
# =========================

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

print(conjunto1 | conjunto2)  # união {1, 2, 3, 4, 5}
print(conjunto1 & conjunto2)  # interseção {3}
print(conjunto1 - conjunto2)  # diferença {1, 2}
print(conjunto1 ^ conjunto2)  # diferença simétrica {1, 2, 4, 5}

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")        # adiciona item
frutas.remove("banana")   # remove (gera erro se não existir)
frutas.discard("uva")     # remove sem erro se não existir
frutas.clear()            # limpa o conjunto