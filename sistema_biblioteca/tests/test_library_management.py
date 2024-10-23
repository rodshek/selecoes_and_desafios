import unittest
import os
from src.library_management import LibraryManagement


class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        self.db_path = 'tests/test_library.db'
        self.library = LibraryManagement(self.db_path)

    def tearDown(self):
        self.library.close()
        os.remove(self.db_path)

    def test_add_book(self):
        self.library.add_book("Livro Teste", "Autor Teste")
        books = self.library.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "Livro Teste")
        self.assertTrue(books[0]['available'])

    def test_borrow_book(self):
        self.library.add_book("Livro Empréstimo", "Autor")
        book_id = self.library.list_books()[0]['id']
        result = self.library.borrow_book(book_id, "Usuário Teste")
        self.assertTrue(result)
        self.assertFalse(self.library.list_books()[0]['available'])

    def test_return_book(self
