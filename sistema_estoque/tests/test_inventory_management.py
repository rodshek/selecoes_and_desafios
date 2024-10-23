import os
import unittest

from src.inventory_management import InventoryManagement


class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        self.db_path = 'tests/test_inventory.db'
        self.inventory = InventoryManagement(self.db_path)

    def tearDown(self):
        self.inventory.close()
        os.remove(self.db_path)

    def test_add_item(self):
        self.inventory.add_item("Item Teste", 10)
        items = self.inventory.list_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['name'], "Item Teste")
        self.assertEqual(items[0]['quantity'], 10)

    def test_remove_item(self):
        self.inventory.add_item("Item Teste", 10)
        item_id = self.inventory.list_items()[0]['id']
        result = self.inventory.remove_item(item_id)
        self.assertTrue(result)
        self.assertEqual(len(self.inventory.list_items()), 0)

    def test_update_item_quantity(self):
        self.inventory.add_item("Item Teste", 10)
        item_id = self.inventory.list_items()[0]['id']
        result = self.inventory.update_item_quantity(item_id, 20)
        self.assertTrue(result)
        self.assertEqual(self.inventory.list_items()[0]['quantity'], 20)


if __name__ == '__main__':
    unittest.main()
