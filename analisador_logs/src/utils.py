def read_log_file(log_file_path):
    """
    Lê o arquivo de log e retorna uma lista de linhas.
    """
    with open(log_file_path, 'r') as log_file:
        return log_file.readlines()
