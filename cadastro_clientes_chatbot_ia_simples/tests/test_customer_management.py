import unittest

from src.customer_management import CustomerManager


class TestCustomerManager(unittest.TestCase):

    def setUp(self):
        self.manager = CustomerManager()

    def test_add_customer(self):
        self.manager.add_customer(
            "Cliente Teste", "teste@email.com", "123456789")
        self.assertEqual(len(self.manager.customers), 1)
        self.assertEqual(self.manager.customers[0]["name"], "Cliente Teste")

    def test_update_customer(self):
        self.manager.add_customer(
            "Cliente Teste", "teste@email.com", "123456789")
        self.manager.update_customer(1, name="Cliente Atualizado")
        self.assertEqual(
            self.manager.customers[0]["name"], "Cliente Atualizado")

    def test_remove_customer(self):
        self.manager.add_customer(
            "Cliente Teste", "teste@email.com", "123456789")
        self.manager.remove_customer(1)
        self.assertEqual(len(self.manager.customers), 0)

    def test_list_customers(self):
        self.manager.add_customer(
            "Cliente Teste", "teste@email.com", "123456789")
        self.manager.list_customers()  # Verifica se a listagem ocorre sem erros


if __name__ == "__main__":
    unittest.main()
