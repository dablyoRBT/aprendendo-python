# =========================
# Importação de módulos import()
# =========================

import math # Importando o módulo math completo, assim temos acesso a varias funções ao digitar-mos math.
resultado = int(math.sqrt(64))
print(resultado)  # Imprime 8

from math import sqrt # Importando função específica de um módulo, assim podemos chamar a própria função sqrt sem o math.
resultado = sqrt(25)
print(resultado)  # Imprime 5

# =========================
# Outros módulos úteis
# =========================

import random # Oferece funções para gerar números aleatórios
import datetime # Permite trabalhar com datas e horas

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual

# =========================
# Criação de módulos próprios que posso usar no meu projeto
# =========================

# Para criar seu módulo você deve criar um arquivo com o nome que desejar ex: meu_modulo.py
# Conteudo do arqv meu_modulo.py
def saudar(nome):
    print(f"Olá, {nome}!")

def calcular_soma(a, b):
    return a + b
'''
# Assim podemos importar o as funções que criamos no outro arquivo
import meu_modulo

meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8
'''

# =========================
# Criação de pacotes
# =========================

# Além da criação de seus próprios módulos você pode criar um pacote -> Nada mais é que uma pasta/diretório que guardara nossos módulos

'''
# O diretório deve conter o arquivo __init__.py que pode até estar vazio esse arquivo defini seu diretório como um pacote python
minhapasta/
    __init__.py
    modulo1.py
    modulo2.py

# Agora podemos importar módulos de maneira mais organizada
from meu_pacote import modulo1, modulo2

modulo1.funcao1()
modulo2.funcao2()

# OBS: Com módulos e pacotes podemos organizar e reutilizar nosso código de maneira eficiente. Modularizando nosso código, temos um código mais legível, estruturado e fácil de manter e entender
'''