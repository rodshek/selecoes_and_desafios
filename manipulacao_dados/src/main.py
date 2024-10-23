from file_processor import process_file

# Resumo do Desafio 1:
# O script faz a leitura de um arquivo de entrada contendo dados brutos, remove duplicatas e ordena as linhas,
# então salva o resultado em um arquivo de saída.

input_file = 'data/arquivo_entrada.txt'
output_file = 'data/arquivo_saida.txt'


def main():
    # Processa o arquivo e gera a saída
    process_file(input_file, output_file)
    print(f"Arquivo processado com sucesso. Saída salva em {output_file}")


if __name__ == "__main__":
    main()

# Explicação:
# O projeto foi resolvido dessa forma para modularizar o código, permitindo fácil manutenção e testes.
# A função principal delega o trabalho de processamento para um módulo separado, file_processor.py,
# garantindo uma abordagem limpa e organizada.
