import os
import json
from dotenv import load_dotenv

from scripts.login import ssh_connect
from view.menu import menu

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
config_path = os.path.join(BASE_DIR, "config.json")

if __name__ == "__main__":
    
    with open(config_path, "r") as f:
        config = json.load(f)

    while True:
        opcoes = menu(config)
        if '0' in opcoes:
            break

        cliente = opcoes[0] # sc, pr, to, ro, pi, am, gm
        servidor = opcoes[1] # web ou mob
        aplicacao = opcoes[2] # mob, ait, etc
        servico = opcoes[3] # socket, gerador, consumidor, etc
        
        logs = config[f"{cliente}"][f"{servidor}"][f"{aplicacao}"][f'{servico}']

        host = os.getenv(f"host_{cliente}_{servidor}".upper())
        user = os.getenv(f"user_{cliente}_{servidor}".upper())
        password = os.getenv(f"password_{cliente}_{servidor}".upper())
        ssh_connect(host, user, password, logs)
