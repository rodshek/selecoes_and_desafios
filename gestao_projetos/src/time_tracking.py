import time


class TimeTracker:
    def __init__(self):
        """
        Inicializa o controle de tempo para projetos.
        """
        self.start_times = {}

    def start_tracking(self, project_id):
        """
        Inicia o rastreamento de tempo de um projeto.

        :param project_id: ID do projeto.
        """
        if project_id in self.start_times:
            print(f"O projeto {project_id} já está sendo rastreado.")
        else:
            self.start_times[project_id] = time.time()
            print(
                f"Rastreamento de tempo para o projeto {project_id} iniciado.")

    def stop_tracking(self, project_id):
        """
        Para o rastreamento de tempo de um projeto e calcula o tempo gasto.

        :param project_id: ID do projeto.
        """
        if project_id in self.start_times:
            elapsed_time = time.time() - self.start_times.pop(project_id)
            print(
                f"Rastreamento de tempo para o projeto {project_id} parado. Tempo total: {elapsed_time:.2f} segundos.")
        else:
            print(
                f"Nenhum rastreamento em andamento para o projeto {project_id}.")
