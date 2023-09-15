import bancoDados
import socket

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
        
            opcao = int(input("Entre com a opção desejada: "))
            if opcao == 1:
                    for index,lista in bancoDados.apolices.items():
                        if usuario == lista[4]:
                            print(lista[0])
                            print(lista[1])
                            print(lista[2])
                            print(lista[3])
                            print(lista[4])
                            print(lista[5])
                    break
            elif opcao == 2:
                print("Falando com o atendente")
        else:
            print("Usuário não cadastrado")

if resposta == 2:
    usuario = input("Digite o nome do Usuário ").title()
    senha = input("Digite a Sua Senha ")
    for index,adm in bancoDados.adm.items():
        if usuario == adm[0] and senha == adm[1]:
            print(f"Ola {usuario} Bem vindo novamente")
            print(f"Escolha uma das opções abaixo para continuar: ")
            print("Digite 1 para ver todos os usuários cadastrados")
            print("Digite 2 para adicionar um novo usuário")
            print("Digite 3 para excluir um usuário")
            print("Digite 4 para procurar um usuário específico")
            print("Digite 5 para Sair")
            opcao = int(input("Entre com a opção desejada: "))

            if opcao == 1:
                for index,usuarios in bancoDados.apolices.items():
                    print (usuarios)
            elif opcao == 2:
                id = list(bancoDados.apolices.keys())
                bancoDados.apolices[id[len(id)-1]+1] = [input("Entre com a nova apólice: ").title(),
                input("Entre com o nome completo: "),
                input("Entre com a data de nascimento incluindo a barra: "),
                input("Entre com o cpf incluindo pontos e traço: "),
                input("Entre com o nome do usuário (Primeira letra Maiuscula): "),
                input("Entre com a senha (Primeira letra Maiuscula): ")]
                for index,lista in bancoDados.apolices.items():
                    print(index,lista)
            elif opcao == 3:
                busca = input("Entre com o Nome do usuário: ").title()
                for index, lista in bancoDados.apolices.items():
                    if busca == lista[0]:
                        del bancoDados.apolices[busca]
                        print(index,lista)
            elif opcao == 4:
                apoliceBuscada = input("Digite o numero da apólice procurada ")
                for index,lista in bancoDados.apolices.items():
                    if apoliceBuscada == lista[0]:
                        print(index,lista)