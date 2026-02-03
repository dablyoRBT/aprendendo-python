projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos:
    if projeto is not None:
        print(f"Projeto: {projeto}")
    else:
        print("Projeto ausente")