import paramiko
import subprocess
import os

from .logs import monitor_logs

def ssh_connect(hostname, username, password, log_file):
    """
    Conecta a um servidor via SSH e inicia o monitoramento de logs.
    """
    try:
        print(f"Conectando a {hostname}...")
        # Cria o cliente SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)

        print("Conexão bem-sucedida!")

        # Inicia o monitoramento de logs
        monitor_logs(ssh, log_file)
    except Exception as e:
        print(f"Erro ao conectar: {e}")