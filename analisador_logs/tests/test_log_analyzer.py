import unittest

from src.log_analyzer import analyze_logs


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        # Simula um arquivo de log para teste
        self.sample_logs = [
            '192.168.1.1 - - [21/Oct/2024:10:00:23 +0000] "GET /index.html HTTP/1.1" 200 2326\n',
            '192.168.1.2 - - [21/Oct/2024:10:01:47 +0000] "POST /form.html HTTP/1.1" 404 4523\n',
            '192.168.1.1 - - [21/Oct/2024:11:00:23 +0000] "GET /about.html HTTP/1.1" 200 2326\n'
        ]

    def test_analyze_logs(self):
        result = analyze_logs(self.sample_logs)

        # Verifica se os IPs mais frequentes estão corretos
        self.assertEqual(result['ips']['192.168.1.1'], 2)
        self.assertEqual(result['ips']['192.168.1.2'], 1)

        # Verifica os códigos de status HTTP
        self.assertEqual(result['statuses']['200'], 2)
        self.assertEqual(result['statuses']['404'], 1)

        # Verifica a contagem de requisições por hora
        self.assertEqual(result['requests_per_hour']['10'], 2)
        self.assertEqual(result['requests_per_hour']['11'], 1)


if __name__ == '__main__':
    unittest.main()
