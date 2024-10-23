import unittest

from src.sales_management import SalesManager


class TestSalesManager(unittest.TestCase):

    def setUp(self):
        self.sales_manager = SalesManager()

    def test_register_sale(self):
        self.sales_manager.register_sale("Produto Teste", 2, 10.0)
        self.assertEqual(len(self.sales_manager.sales), 1)
        self.assertEqual(
            self.sales_manager.sales[0]["product"], "Produto Teste")

    def test_list_sales(self):
        self.sales_manager.register_sale("Produto Teste", 2, 10.0)
        self.assertEqual(self.sales_manager.sales[0]["total_price"], 20.0)


if __name__ == "__main__":
    unittest.main()
