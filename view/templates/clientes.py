import sys

def clientes(opcoes):
    while True:
        print("\n=================================")
        print("Qual cliente você deseja acessar?")
        print("1 - Paraná")
        print("2 - Santa Catarina")
        print("3 - Rondonia")
        print("4 - Tocantins")
        print("0 - Sair")
        cliente = input("Digite a opção desejada: ")
        # opcoes[0]
        match cliente:
                case '0':
                    print("\033[93mSAINDO DO SISTEMA...\033[0m")
                    sys.exit()
                case '1':
                    opcoes.append('pr')
                    break
                case '2':
                    opcoes.append('sc')
                    break
                case '3':
                    opcoes.append('ro')
                    break
                case '4':
                    opcoes.append('to')
                    break
                case _:
                    print("\033[91mOpção inválida. Tente novamente.\033[0m")
