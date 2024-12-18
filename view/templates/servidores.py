import sys

def servidores(opcoes):
    while True:
        print("\n=================================")
        print("Qual servidor você deseja acessar?")
        print("1 - Mobile")
        print("2 - Web")
        print("0 - Sair")
        servidor = input("Digite a opção desejada: ")
        # opcoes[1]
        match servidor:
                case '0':
                    print("\033[93mSAINDO DO SISTEMA...\033[0m")
                    sys.exit()
                case '1':
                    opcoes.append('mob')
                    break
                case '2':
                    opcoes.append('web')
                    break
                case _:
                    print("\033[91mOpção inválida. Tente novamente.\033[0m")
    