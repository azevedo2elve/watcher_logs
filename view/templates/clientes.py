import sys

def clientes(opcoes, config):
    while True:
        configuracao = list(config.keys())
        print(f"Configuração: {configuracao}")
        print("\n=================================")
        print("Qual cliente você deseja acessar?")
        for i, key in enumerate(configuracao, start=1):
                display_name = key.upper()
                print(f"{i} - {display_name}")
        print("0 - Sair")
        cliente = input("Digite a opção desejada: ")
        try:
            cliente = int(cliente)
            if cliente == 0:
                print("\033[93mSAINDO DO SISTEMA...\033[0m")
                sys.exit()

            for i, key in enumerate(configuracao, start=1):
                choose_name = key
                if cliente == i:
                    opcoes.append(choose_name)
                    print(f"Você escolheu: {choose_name.upper()}")
                    break
            else:
                print("\033[91mOpção inválida. Tente novamente.\033[0m")
                continue

            break
        except ValueError:
            print("\033[91mOpção inválida. Por favor, digite um número.\033[0m")
