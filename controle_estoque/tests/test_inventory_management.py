import unittest

from src.inventory_management import InventoryManager


class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.manager = InventoryManager()

    def test_add_product(self):
        self.manager.add_product("Produto Teste", 10, 5.0)
        self.assertIn("Produto Teste", self.manager.inventory)
        self.assertEqual(
            self.manager.inventory["Produto Teste"]["quantity"], 10)

    def test_update_quantity(self):
        self.manager.add_product("Produto Teste", 10, 5.0)
        self.manager.update_quantity("Produto Teste", 20)
        self.assertEqual(
            self.manager.inventory["Produto Teste"]["quantity"], 20)

    def test_view_inventory(self):
        self.manager.add_product("Produto Teste", 10, 5.0)
        self.manager.view_inventory()  # Testa se o método não gera erros


if __name__ == "__main__":
    unittest.main()
