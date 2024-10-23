import unittest

from src.sales_management import SalesManager


class TestSalesManager(unittest.TestCase):

    def setUp(self):
        self.manager = SalesManager()

    def test_register_sale(self):
        self.manager.register_sale("Produto Teste", 10, 5.0)
        self.assertEqual(len(self.manager.sales), 1)
        self.assertEqual(
            self.manager.sales[0]["product_name"], "Produto Teste")
        self.assertEqual(self.manager.sales[0]["total_value"], 50.0)

    def test_get_sales_data(self):
        self.manager.register_sale("Produto Teste", 10, 5.0)
        sales_data = self.manager.get_sales_data()
        self.assertEqual(len(sales_data), 1)
        self.assertEqual(sales_data[0]["product_name"], "Produto Teste")


if __name__ == "__main__":
    unittest.main()
