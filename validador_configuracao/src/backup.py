import os
import shutil

from utils import is_file_modified


def incremental_backup(original_dir, backup_dir):
    # Cria o diretório de backup, se não existir
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Itera sobre os arquivos no diretório original
    for root, _, files in os.walk(original_dir):
        for file in files:
            original_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(original_file_path, original_dir)
            backup_file_path = os.path.join(backup_dir, relative_path)

            # Verifica se o arquivo é novo ou foi modificado
            if not os.path.exists(backup_file_path) or is_file_modified(original_file_path, backup_file_path):
                backup_subdir = os.path.dirname(backup_file_path)
                if not os.path.exists(backup_subdir):
                    os.makedirs(backup_subdir)
                shutil.copy2(original_file_path, backup_file_path)
                print(f"Arquivo {relative_path} copiado para backup.")
