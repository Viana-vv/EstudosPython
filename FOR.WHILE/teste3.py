projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projto in projetos:
    if projto is None:
        print("Projeto não definido.")
    else:
        print(f"Trabalhando no projeto: {projto}")