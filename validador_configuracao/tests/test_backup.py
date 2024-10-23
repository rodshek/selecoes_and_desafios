import os
import shutil
import unittest

from src.backup import incremental_backup


class TestBackup(unittest.TestCase):

    def setUp(self):
        # Configura diretórios temporários para teste
        self.original_dir = 'tests/original_test_dir'
        self.backup_dir = 'tests/backup_test_dir'

        # Cria o diretório original de teste
        os.makedirs(self.original_dir, exist_ok=True)
        with open(os.path.join(self.original_dir, 'file1.txt'), 'w') as f:
            f.write('Este é o arquivo 1.')

    def tearDown(self):
        # Remove os diretórios de teste após cada teste
        shutil.rmtree(self.original_dir)
        shutil.rmtree(self.backup_dir)

    def test_incremental_backup(self):
        # Executa o backup incremental
        incremental_backup(self.original_dir, self.backup_dir)

        # Verifica se o arquivo foi copiado corretamente
        backup_file_path = os.path.join(self.backup_dir, 'file1.txt')
        self.assertTrue(os.path.exists(backup_file_path))


if __name__ == '__main__':
    unittest.main()
