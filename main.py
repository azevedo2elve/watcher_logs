import os
import json
from dotenv import load_dotenv

from scripts.login import ssh_connect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
config_path = os.path.join(BASE_DIR, "config.json")

if __name__ == "__main__":

    # Paraná
    host_pr_mob = os.getenv("HOST_PR_MOB")
    host_pr_web = os.getenv("HOST_PR_WEB")
    user_pr = os.getenv("USER_PR")
    password_pr = os.getenv("PASSWORD_PR")

    # Santa Catarina
    host_sc_mob = os.getenv("host_sc_mob".upper())
    host_sc_web = os.getenv("host_sc_mob".upper())
    user_sc = os.getenv("user_sc")
    password_sc = os.getenv("password_sc")
    
    with open(config_path, "r") as f:
        config = json.load(f)

    def menu():
        opcoes = []

        # Menu dos clientes
        while True:
            print("\n=================================")
            print("Qual cliente você deseja acessar?")
            print("1 - Paraná")
            print("2 - Santa Catarina")
            print("0 - Sair")
            cliente = input("Digite a opção desejada: ")
            # opcoes[0]
            match cliente:
                    case '0':
                        print("\033[93mSAINDO DO SISTEMA...\033[0m")
                        return ['0']
                    case '1':
                        opcoes.append('pr')
                        break
                    case '2':
                        opcoes.append('sc')
                        break
                    case _:
                        print("\033[91mOpção inválida. Tente novamente.\033[0m")         

        # Menu dos servidores    
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
                        return ['0']
                    case '1':
                        opcoes.append('mob')
                        break
                    case '2':
                        opcoes.append('web')
                        break
                    case _:
                        print("\033[91mOpção inválida. Tente novamente.\033[0m")
        
        if servidor == '1' and (cliente == '1' or cliente == '2'):
            while True:
                print("\n=================================")
                print("Qual serviço MOBILE deseja acessar?")
                print("1 - Socket")
                print("2 - Consumidor")
                print("3 - Consumidor Baixa Prioridade")
                print("4 - Gerador")
                print("5 - Gerador2")
                print("6 - Gerador3")
                print("7 - Socket Files")
                print("8 - Controle Frames")
                print("0 - Sair")
                servidor = input("Digite a opção desejada: ")
                match servidor:
                    case '0':
                        print("\033[93mSAINDO DO SISTEMA...\033[0m")
                    case '1':
                        opcoes.append('socket')
                        break
                    case '2':
                        opcoes.append('consumidor')
                        break
                    case '3':
                        opcoes.append('consumidor_baixa')
                        break
                    case '4':
                        opcoes.append('gerador')
                        break
                    case '5':
                        opcoes.append('gerador2')
                        break
                    case '6':
                        opcoes.append('gerador3')
                        break
                    case '7':
                        opcoes.append('socket_files')
                        break
                    case '8':
                        opcoes.append('controle_frames')
                        break
                    case _:
                        print("\033[91mOpção inválida. Tente novamente.\033[0m")
                if servidor == '0':
                    return ['0']
        elif servidor == '2':
            while True:
                print("\n=================================")
                print("Qual log WEB deseja acessar?")
                print("1 - Sade Access")
                print("2 - Sade Access SSL")
                print("3 - Sade Error")
                print("4 - Sade Error SSL")
                print("0 - Sair")
                servidor = input("Digite a opção desejada: ")
                match servidor:
                    case '0':
                        print("\033[93mSAINDO DO SISTEMA...\033[0m")
                    case '1':
                        opcoes.append('sade_access')
                        break
                    case '2':
                        opcoes.append('sade_access_ssl')
                        break
                    case '3':
                        opcoes.append('sade_error')
                        break
                    case '4':
                        opcoes.append('sade_error_ssl')
                        break
                    case _:
                        print("\033[91mOpção inválida. Tente novamente.\033[0m")
                if servidor == '0':
                    return ['0']

        return opcoes

    while True:
        opcoes = menu()
        if '0' in opcoes:
            break

        cliente = opcoes[0] # sc, pr, to, ro, pi, am, gm
        servidor = opcoes[1] # web ou mob
        servico = opcoes[2] # socket, gerador, consumidor, etc
        logs_mobile = config[f"logs_{servidor}_{cliente}"][f'{servico}']

        host = os.getenv(f"host_{cliente}_{servidor}".upper())
        user = os.getenv(f"user_{cliente}".upper())
        password = os.getenv(f"password_{cliente}_{servidor}".upper())
        ssh_connect(host, user, password, logs_mobile)
