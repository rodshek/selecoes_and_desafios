import unittest

from src.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task("Tarefa Teste", 3)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0]["title"], "Tarefa Teste")

    def test_edit_task(self):
        self.task_manager.add_task("Tarefa Teste", 3)
        self.task_manager.edit_task(1, "Tarefa Editada", 5)
        self.assertEqual(self.task_manager.tasks[0]["title"], "Tarefa Editada")
        self.assertEqual(self.task_manager.tasks[0]["priority"], 5)

    def test_remove_task(self):
        self.task_manager.add_task("Tarefa Teste", 3)
        self.task_manager.remove_task(1)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_mark_task_completed(self):
        self.task_manager.add_task("Tarefa Teste", 3)
        self.task_manager.mark_task_completed(1)
        self.assertTrue(self.task_manager.tasks[0]["completed"])

    def test_find_task(self):
        self.task_manager.add_task("Tarefa Teste", 3)
        task = self.task_manager._find_task(1)
        self.assertIsNotNone(task)
        self.assertEqual(task["title"], "Tarefa Teste")


if __name__ == "__main__":
    unittest.main()
