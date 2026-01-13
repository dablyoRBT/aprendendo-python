# =========================
# Input()
# =========================

# Lembre-se que por padrão o input trabalha com strings ou seja se quiser usar outros tipos de dados especifique int(), float()...
nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
print("Olá, " + nome + "!")
print(f"Você tem {idade} anos.") # Durante a saida de dados podemos usar "f-string" ou separar a variavel(dados) da string""

# =========================
# Leitura e edição de arquivos em python
# =========================

# Para lêr um arquivo usamos a função open() em modo de leitura ("r"). Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines() e por fim close() para fechar o arquivo
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()
