import sys

from backup import incremental_backup

# Resumo do Desafio 2:
# Este script realiza um backup incremental, copiando apenas arquivos novos ou modificados
# de um diretório de origem para um diretório de backup.


def main():
    if len(sys.argv) != 3:
        print("Uso: python src/main.py <caminho_diretorio_original> <caminho_diretorio_backup>")
        sys.exit(1)

    original_dir = sys.argv[1]
    backup_dir = sys.argv[2]

    incremental_backup(original_dir, backup_dir)
    print(f"Backup incremental realizado de {original_dir} para {backup_dir}.")


if __name__ == "__main__":
    main()

# Explicação:
# O script recebe dois parâmetros: o diretório original e o diretório de backup.
# Utilizamos a função incremental_backup do módulo backup.py, que faz a cópia de
# arquivos apenas se eles forem novos ou modificados.
