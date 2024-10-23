import sqlite3


class EmployeeDatabase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        """
        Cria a tabela de funcionários se ela ainda não existir.
        """
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            cargo TEXT NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_employee(self, nome, idade, cargo):
        """
        Adiciona um novo funcionário ao banco de dados.
        """
        query = "INSERT INTO employees (nome, idade, cargo) VALUES (?, ?, ?);"
        self.conn.execute(query, (nome, idade, cargo))
        self.conn.commit()

    def update_employee(self, employee_id, nome, idade, cargo):
        """
        Atualiza os dados de um funcionário existente.
        """
        query = "UPDATE employees SET nome = ?, idade = ?, cargo = ? WHERE id = ?;"
        self.conn.execute(query, (nome, idade, cargo, employee_id))
        self.conn.commit()

    def list_employees(self):
        """
        Retorna todos os funcionários cadastrados.
        """
        query = "SELECT * FROM employees;"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def remove_employee(self, employee_id):
        """
        Remove um funcionário do banco de dados.
        """
        query = "DELETE FROM employees WHERE id = ?;"
        self.conn.execute(query, (employee_id,))
        self.conn.commit()

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.conn.close()
