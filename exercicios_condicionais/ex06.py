from datetime import datetime

entrada = datetime.now()

if entrada.hour > 8 and entrada.hour < 18:
    print("Seja bem vindo!")
else:
    print("Fora do horário de atendimento. Acesso negado!")