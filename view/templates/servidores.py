import sys

def servidores(opcoes, config):
    # while True:
    #     print("\n=================================")
    #     print("Qual servidor você deseja acessar?")
    #     print("1 - Mobile")
    #     print("2 - Web")
    #     print("0 - Sair")
    #     servidor = input("Digite a opção desejada: ")
    #     # opcoes[1]
    #     match servidor:
    #             case '0':
    #                 print("\033[93mSAINDO DO SISTEMA...\033[0m")
    #                 sys.exit()
    #             case '1':
    #                 opcoes.append('mob')
    #                 break
    #             case '2':
    #                 opcoes.append('web')
    #                 break
    #             case _:
    #                 print("\033[91mOpção inválida. Tente novamente.\033[0m")
    while True:
            configuracao = config[f"{opcoes[0]}"]
            print("\n=================================")
            print("Qual servidor você deseja acessar?")
            for i, (key, value) in enumerate(configuracao.items(), start=1):
                display_name = key.replace("logs_", "").upper()
                print(f"{i} - {display_name}")
            print("0 - Sair")
            servico = input("Digite a opção desejada: ")
            try:
                servico = int(servico)
                if servico == 0:
                    print("\033[93mSAINDO DO SISTEMA...\033[0m")
                    sys.exit()

                for i, (key, value) in enumerate(configuracao.items(), start=1):
                    choose_name = key
                    if servico == i:
                        opcoes.append(choose_name)
                        print(f"Você escolheu: {choose_name.upper()}")
                        break
                else:
                    print("\033[91mOpção inválida. Tente novamente.\033[0m")
                    continue

                break
            except ValueError:
                print("\033[91mOpção inválida. Por favor, digite um número.\033[0m")
    