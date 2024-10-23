desafio_01_manipulacao_dados
│
├── README.md                # Documentação do projeto
├── requirements.txt         # Bibliotecas necessárias
├── data
│   ├── arquivo_entrada.txt  # Arquivo grande de entrada
│   ├── arquivo_saida.txt    # Arquivo de saída (após o processamento)
│
├── src
│   ├── main.py              # Script principal
│   ├── file_processor.py    # Módulo que contém a lógica de processamento de dados
│
└── tests
    └── test_file_processor.py # Testes unitários para verificar o processamento

# Desafio 01: Manipulação de Dados

## Descrição do Projeto

Este projeto realiza a leitura de um arquivo de texto de grande porte, processa seus dados (remove duplicatas e ordena) e escreve o resultado em um arquivo de saída.

### Estrutura do Projeto

- **data/arquivo_entrada.txt**: Arquivo de entrada com os dados brutos.
- **data/arquivo_saida.txt**: Arquivo de saída com os dados processados.
- **src/main.py**: Script principal que orquestra a leitura, processamento e escrita dos dados.
- **src/file_processor.py**: Módulo que contém a lógica de processamento dos dados.
- **tests/test_file_processor.py**: Testes unitários para verificar se o processamento de dados está funcionando corretamente.

### Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
