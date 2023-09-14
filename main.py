import bancoDados

resposta = int(input("Seja bem vindo(a) escolha uma das opções abaixo para continuar 1-Entrar 2-Sou ADM 3-Cancelar "))

if resposta==1:
    usuario = input("Digite o nome do Usuário ").title()
    senha = input("Digite a Sua Senha ")
    for index,lista in bancoDados.apolices.items():
        if usuario == lista[4] and senha == lista[5]:
            print(f"Ola {usuario} Bem vindo novamente")
            print(f"Escolha uma das opções abaixo para continuar: ")
            print("Digite 1 para ver suas informações")
            print("Digite 2 para Falar com o Atendente")
        else:
            print("Usuário não cadastrado")