import unittest

from src.product_management import ProductManagement


class TestProductManagement(unittest.TestCase):

    def setUp(self):
        self.manager = ProductManagement()

    def test_add_product(self):
        self.manager.add_product("Produto A", 10.0, 5)
        products = self.manager.list_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]['name'], "Produto A")

    def test_update_product(self):
        self.manager.add_product("Produto B", 20.0, 10)
        updated = self.manager.update_product(
            1, name="Produto B Atualizado", price=25.0)
        self.assertTrue(updated)
        product = self.manager.list_products()[0]
        self.assertEqual(product['name'], "Produto B Atualizado")
        self.assertEqual(product['price'], 25.0)

    def test_remove_product(self):
        self.manager.add_product("Produto C", 30.0, 15)
        removed = self.manager.remove_product(1)
        self.assertTrue(removed)
        self.assertEqual(len(self.manager.list_products()), 0)


if __name__ == '__main__':
    unittest.main()
