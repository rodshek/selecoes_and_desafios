# Desafio 02: Backup Incremental

## Descrição do Projeto

Este projeto implementa um sistema de backup incremental. A solução compara arquivos entre o diretório original e o diretório de backup e copia apenas os arquivos modificados ou novos, economizando tempo e espaço.

### Estrutura do Projeto

- **src/main.py**: Script principal que orquestra o processo de backup incremental.
- **src/backup.py**: Módulo que contém a lógica principal do backup incremental.
- **src/utils.py**: Funções auxiliares, como comparação de arquivos e diretórios.
- **backup/**: Diretório onde os backups incrementais serão salvos.
- **tests/test_backup.py**: Testes unitários para verificar o comportamento do backup incremental.

### Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
