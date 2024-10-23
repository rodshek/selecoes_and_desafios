class ProjectManager:
    def __init__(self):
        """
        Inicializa o gerenciador de projetos com uma lista vazia.
        """
        self.projects = []
        self.project_id_counter = 1

    def create_project(self, name, description, deadline):
        """
        Cria um novo projeto e o adiciona à lista.

        :param name: Nome do projeto.
        :param description: Descrição do projeto.
        :param deadline: Data de entrega do projeto.
        """
        project = {
            "id": self.project_id_counter,
            "name": name,
            "description": description,
            "deadline": deadline,
            "status": "Em andamento"
        }
        self.projects.append(project)
        self.project_id_counter += 1
        print(f"Projeto '{name}' criado com sucesso!")

    def update_project_status(self, project_id, status):
        """
        Atualiza o status de um projeto existente.

        :param project_id: ID do projeto.
        :param status: Novo status do projeto.
        """
        for project in self.projects:
            if project["id"] == project_id:
                project["status"] = status
                print(
                    f"Status do projeto '{project['name']}' atualizado para '{status}'.")
                return
        print(f"Projeto com ID {project_id} não encontrado.")

    def list_projects(self):
        """
        Lista todos os projetos cadastrados.
        """
        if not self.projects:
            print("Nenhum projeto cadastrado.")
        else:
            print("\nProjetos Registrados:")
            for project in self.projects:
                print(
                    f"ID: {project['id']}, Nome: {project['name']}, Status: {project['status']}, Data de entrega: {project['deadline']}")
