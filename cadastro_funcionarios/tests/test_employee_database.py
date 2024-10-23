import os
import unittest

from src.employee_database import EmployeeDatabase


class TestEmployeeDatabase(unittest.TestCase):

    def setUp(self):
        # Cria um banco de dados temporário para teste
        self.db_path = 'tests/test_funcionarios.db'
        self.db = EmployeeDatabase(self.db_path)

    def tearDown(self):
        # Remove o banco de dados após os testes
        self.db.close()
        os.remove(self.db_path)

    def test_add_employee(self):
        self.db.add_employee("John Doe", 30, "Desenvolvedor")
        employees = self.db.list_employees()
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0][1], "John Doe")

    def test_update_employee(self):
        self.db.add_employee("John Doe", 30, "Desenvolvedor")
        employee_id = self.db.list_employees()[0][0]
        self.db.update_employee(employee_id, "Jane Doe", 32, "Gerente")
        updated_employee = self.db.list_employees()[0]
        self.assertEqual(updated_employee[1], "Jane Doe")
        self.assertEqual(updated_employee[2], 32)

    def test_remove_employee(self):
        self.db.add_employee("John Doe", 30, "Desenvolvedor")
        employee_id = self.db.list_employees()[0][0]
        self.db.remove_employee(employee_id)
        employees = self.db.list_employees()
        self.assertEqual(len(employees), 0)


if __name__ == '__main__':
    unittest.main()
