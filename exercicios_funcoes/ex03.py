from datetime import datetime



def saudar(nome):
    hora = datetime.now().hour
    if 5 <= hora < 12:
        return f"Bom dia, {nome}!"
    elif 12 <= hora < 18:
        return f"Boa tarde, {nome}!"
    else:
        return f"Boa noite, {nome}!"
    
print(saudar("Carlos"))