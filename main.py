import os
import json
from dotenv import load_dotenv

from scripts.login import ssh_connect
from view.menu import menu

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

    while True:
        opcoes = menu(config)
        print(opcoes)
        if '0' in opcoes:
            break

        print(opcoes)
        cliente = opcoes[0] # sc, pr, to, ro, pi, am, gm
        servidor = opcoes[1] # web ou mob
        aplicacao = opcoes[2] # mob, ait, etc
        servico = opcoes[3] # socket, gerador, consumidor, etc
        
        logs = config[f"{cliente}"][f"{servidor}"][f"{aplicacao}"][f'{servico}']

        host = os.getenv(f"host_{cliente}_{servidor}".upper())
        user = os.getenv(f"user_{cliente}".upper())
        password = os.getenv(f"password_{cliente}_{servidor}".upper())
        ssh_connect(host, user, password, logs)
