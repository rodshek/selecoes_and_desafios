# Desafio 03: Analisador de Logs

## Descrição do Projeto

Este projeto implementa um analisador de arquivos de logs, que extrai informações úteis como:
- IPs mais frequentes
- Códigos de status HTTP
- Contagem de requisições por hora

### Estrutura do Projeto

- **src/main.py**: Script principal que orquestra a análise dos arquivos de log.
- **src/log_analyzer.py**: Módulo com a lógica para analisar os logs.
- **src/utils.py**: Funções auxiliares, como formatação e leitura de arquivos.
- **logs/**: Diretório onde os arquivos de logs são armazenados.
- **tests/test_log_analyzer.py**: Testes unitários para garantir que a análise de logs está correta.

### Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
