def monitor_logs(ssh, log_file):
    """
    Executa os comandos remotamente e exibe os logs.
    """
    try:
        print(f"Monitorando logs em: {log_file}")
        stdin, stdout, stderr = ssh.exec_command(f"{log_file}")

        # Exibe os logs em tempo real
        for line in iter(stdout.readline, ""):
            print(line, end="")
    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuário.")
    finally:
        ssh.close()
        print("Conexão encerrada.")