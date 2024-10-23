import sqlite3


class LibraryManagement:
    def __init__(self, db_path='library.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        """
        Cria as tabelas necessárias no banco de dados.
        """
        query_books = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            available INTEGER NOT NULL DEFAULT 1
        );
        """
        query_loans = """
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            borrower TEXT NOT NULL,
            date_loaned DATE DEFAULT (DATE('now')),
            date_returned DATE,
            FOREIGN KEY (book_id) REFERENCES books(id)
        );
        """
        self.conn.execute(query_books)
        self.conn.execute(query_loans)
        self.conn.commit()

    def add_book(self, title, author):
        """
        Adiciona um novo livro ao catálogo.
        """
        query = "INSERT INTO books (title, author) VALUES (?, ?);"
        self.conn.execute(query, (title, author))
        self.conn.commit()

    def list_books(self):
        """
        Lista todos os livros disponíveis no catálogo.
        """
        query = "SELECT id, title, author, available FROM books;"
        cursor = self.conn.execute(query)
        books = cursor.fetchall()
        return [{'id': row[0], 'title': row[1], 'author': row[2], 'available': bool(row[3])} for row in books]

    def borrow_book(self, book_id, borrower):
        """
        Realiza o empréstimo de um livro se ele estiver disponível.
        """
        book = self.get_book_by_id(book_id)
        if book and book['available']:
            query_loan = "INSERT INTO loans (book_id, borrower) VALUES (?, ?);"
            query_update = "UPDATE books SET available = 0 WHERE id = ?;"
            self.conn.execute(query_loan, (book_id, borrower))
            self.conn.execute(query_update, (book_id,))
            self.conn.commit()
            return True
        return False

    def return_book(self, book_id):
        """
        Realiza a devolução de um livro e o marca como disponível.
        """
        book = self.get_book_by_id(book_id)
        if book and not book['available']:
            query_return = "UPDATE loans SET date_returned = DATE('now') WHERE book_id = ? AND date_returned IS NULL;"
            query_update = "UPDATE books SET available = 1 WHERE id = ?;"
            self.conn.execute(query_return, (book_id,))
            self.conn.execute(query_update, (book_id,))
            self.conn.commit()
            return True
        return False

    def get_book_by_id(self, book_id):
        """
        Retorna um livro pelo seu ID.
        """
        query = "SELECT id, title, author, available FROM books WHERE id = ?;"
        cursor = self.conn.execute(query, (book_id,))
        book = cursor.fetchone()
        if book:
            return {'id': book[0], 'title': book[1], 'author': book[2], 'available': bool(book[3])}
        return None

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.conn.close()
