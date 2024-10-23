import unittest

from src.project_management import ProjectManager


class TestProjectManager(unittest.TestCase):

    def setUp(self):
        self.manager = ProjectManager()

    def test_create_project(self):
        self.manager.create_project(
            "Projeto Teste", "Descrição teste", "2024-12-31")
        self.assertEqual(len(self.manager.projects), 1)

    def test_update_project_status(self):
        self.manager.create_project(
            "Projeto Teste", "Descrição teste", "2024-12-31")
        self.manager.update_project_status(1, "Concluído")
        self.assertEqual(self.manager.projects[0]["status"], "Concluído")

    def test_list_projects(self):
        self.manager.create_project(
            "Projeto Teste", "Descrição teste", "2024-12-31")
        # Teste básico para verificar se a listagem ocorre sem erros
        self.manager.list_projects()


if __name__ == "__main__":
    unittest.main()
