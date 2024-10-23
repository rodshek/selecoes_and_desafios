from log_analyzer import analyze_logs

# Resumo do Desafio 3:
# O script faz a leitura de arquivos de logs, extrai informações como IPs mais frequentes,
# códigos de status HTTP, e a quantidade de requisições por hora.


def main():
    log_file = 'logs/exemplo.log'

    print(f"Analisando o arquivo de log: {log_file}\n")
    result = analyze_logs(log_file)

    print("IPs mais frequentes:")
    for ip, count in result['ips'].most_common(5):
        print(f"{ip}: {count} vezes")

    print("\nCódigos de status HTTP mais comuns:")
    for status, count in result['statuses'].items():
        print(f"{status}: {count} vezes")

    print("\nRequisições por hora:")
    for hour, count in result['requests_per_hour'].items():
        print(f"{hour}: {count} requisições")


if __name__ == "__main__":
    main()

# Explicação:
# O script principal foi estruturado para ser simples de usar. Ele chama a função analyze_logs
# do módulo log_analyzer.py para processar o arquivo de log e imprime os resultados no terminal.
