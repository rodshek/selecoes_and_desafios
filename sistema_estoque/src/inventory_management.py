import sqlite3


class InventoryManagement:
    def __init__(self, db_path='inventory.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        """
        Cria as tabelas necessárias no banco de dados.
        """
        query = """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_item(self, name, quantity):
        """
        Adiciona um novo item ao estoque.
        """
        query = "INSERT INTO inventory (name, quantity) VALUES (?, ?);"
        self.conn.execute(query, (name, quantity))
        self.conn.commit()

    def remove_item(self, item_id):
        """
        Remove um item do estoque.
        """
        query = "DELETE FROM inventory WHERE id = ?;"
        cursor = self.conn.execute(query, (item_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def update_item_quantity(self, item_id, quantity):
        """
        Atualiza a quantidade de um item no estoque.
        """
        query = "UPDATE inventory SET quantity = ? WHERE id = ?;"
        cursor = self.conn.execute(query, (quantity, item_id))
        self.conn.commit()
        return cursor.rowcount > 0

    def list_items(self):
        """
        Lista todos os itens no estoque.
        """
        query = "SELECT id, name, quantity FROM inventory;"
        cursor = self.conn.execute(query)
        items = cursor.fetchall()
        return [{'id': row[0], 'name': row[1], 'quantity': row[2]} for row in items]

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.conn.close()
