import os


def is_file_modified(original_file, backup_file):
    """
    Compara as datas de modificação dos arquivos para verificar se o arquivo original foi alterado.
    """
    original_mod_time = os.path.getmtime(original_file)
    backup_mod_time = os.path.getmtime(backup_file)
    return original_mod_time > backup_mod_time
