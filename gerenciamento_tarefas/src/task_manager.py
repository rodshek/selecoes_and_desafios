class TaskManager:
    def __init__(self):
        """
        Inicializa o gerenciador de tarefas com uma lista vazia.
        """
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, priority):
        """
        Adiciona uma nova tarefa.

        :param title: Título da tarefa.
        :param priority: Prioridade da tarefa.
        """
        task = {
            "id": self.task_id_counter,
            "title": title,
            "priority": priority,
            "completed": False
        }
        self.tasks.append(task)
        self.task_id_counter += 1
        print(f"Tarefa '{title}' adicionada com sucesso.")

    def list_tasks(self):
        """
        Lista todas as tarefas.
        """
        if not self.tasks:
            print("Nenhuma tarefa cadastrada.")
            return

        for task in self.tasks:
            status = "Concluída" if task["completed"] else "Pendente"
            print(
                f"ID: {task['id']} | Título: {task['title']} | Prioridade: {task['priority']} | Status: {status}")

    def edit_task(self, task_id, new_title, new_priority):
        """
        Edita uma tarefa existente.

        :param task_id: ID da tarefa a ser editada.
        :param new_title: Novo título da tarefa.
        :param new_priority: Nova prioridade da tarefa.
        """
        task = self._find_task(task_id)
        if task:
            task["title"] = new_title
            task["priority"] = new_priority
            print(f"Tarefa ID {task_id} atualizada com sucesso.")
        else:
            print(f"Tarefa com ID {task_id} não encontrada.")

    def remove_task(self, task_id):
        """
        Remove uma tarefa.

        :param task_id: ID da tarefa a ser removida.
        """
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Tarefa ID {task_id} removida com sucesso.")
        else:
            print(f"Tarefa com ID {task_id} não encontrada.")

    def mark_task_completed(self, task_id):
        """
        Marca uma tarefa como concluída.

        :param task_id: ID da tarefa a ser marcada como concluída.
        """
        task = self._find_task(task_id)
        if task:
            task["completed"] = True
            print(f"Tarefa ID {task_id} marcada como concluída.")
        else:
            print(f"Tarefa com ID {task_id} não encontrada.")

    def _find_task(self, task_id):
        """
        Encontra uma tarefa pelo ID.

        :param task_id: ID da tarefa a ser encontrada.
        :return: A tarefa encontrada ou None.
        """
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
