class TaskManager:
    def __init__(self):
        """
        Inicializa o gerenciador de tarefas com uma lista vazia.
        """
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, description, date):
        """
        Adiciona uma nova tarefa à lista.

        :param title: Título da tarefa.
        :param description: Descrição da tarefa.
        :param date: Data da tarefa.
        """
        task = {
            "id": self.task_id_counter,
            "title": title,
            "description": description,
            "date": date
        }
        self.tasks.append(task)
        self.task_id_counter += 1
        print(f"Tarefa '{title}' adicionada com sucesso!")

    def remove_task(self, task_id):
        """
        Remove uma tarefa com base no ID.

        :param task_id: ID da tarefa a ser removida.
        """
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        print(f"Tarefa com ID {task_id} removida com sucesso.")

    def list_tasks(self):
        """
        Lista todas as tarefas com suas informações.
        """
        if not self.tasks:
            print("Nenhuma tarefa registrada.")
        else:
            print("\nTarefas Registradas:")
            for task in self.tasks:
                print(
                    f"ID: {task['id']}, Título: {task['title']}, Data: {task['date']}, Descrição: {task['description']}")

    def get_task(self, task_id):
        """
        Retorna uma tarefa pelo seu ID.

        :param task_id: ID da tarefa.
        :return: A tarefa correspondente ou None.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        print(f"Tarefa com ID {task_id} não encontrada.")
        return None
