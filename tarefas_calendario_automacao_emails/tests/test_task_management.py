import unittest

from src.task_management import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Tarefa Teste", "Descrição teste", "2024-10-21")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_remove_task(self):
        self.manager.add_task("Tarefa Teste", "Descrição teste", "2024-10-21")
        self.manager.remove_task(1)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_list_tasks(self):
        self.manager.add_task("Tarefa Teste", "Descrição teste", "2024-10-21")
        self.manager.list_tasks()  # Teste básico para verificar se a listagem ocorre sem erros


if __name__ == "__main__":
    unittest.main()
