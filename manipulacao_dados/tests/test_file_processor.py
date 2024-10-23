import unittest

from src.file_processor import process_file


class TestFileProcessor(unittest.TestCase):

    def test_process_file(self):
        # Arquivo de entrada e saída temporários
        input_file = 'tests/test_input.txt'
        output_file = 'tests/test_output.txt'

        # Criando um arquivo de entrada temporário
        with open(input_file, 'w') as f:
            f.write("123, John Doe, 5000\n")
            f.write("456, Jane Smith, 6000\n")
            f.write("123, John Doe, 5000\n")

        # Executando o processamento
        process_file(input_file, output_file)

        # Verificando o conteúdo do arquivo de saída
        with open(output_file, 'r') as f:
            output = f.readlines()

        expected_output = ["123, John Doe, 5000\n", "456, Jane Smith, 6000\n"]
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
