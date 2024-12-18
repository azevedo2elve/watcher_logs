import sys
from .templates.clientes import clientes
from .templates.servidores import servidores

def menu(config):
    opcoes = []

    # print(config.keys())

    # opcoes[0] sc, pr, to, etc CLIENTE
    clientes(opcoes)
    if '0' in opcoes:
        return '0'     
    print(opcoes)

    # opcoes[1] mob ou web SERVIDOR
    servidores(opcoes, config)
    if '0' in opcoes:
        return '0'
    print(opcoes)  
    
    #opcoes[2] mobile, ait, gestao APLICAÇÃO
    while True:
        configuracao = config[f"{opcoes[0]}"][f"{opcoes[1]}"]
        print("\n=================================")
        print(f"Qual aplicação do {opcoes[1]} deseja acessar?")
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
    
    #opcoes[3] socket, etc
    while True:
        configuracao = config[f"{opcoes[0]}"][f"{opcoes[1]}"][f"{opcoes[2]}"]
        print("\n=================================")
        print("Qual aplicação MOBILE deseja acessar?")
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

    return opcoes