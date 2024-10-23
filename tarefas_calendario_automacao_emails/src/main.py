from calendar_integration import CalendarIntegration
from task_management import TaskManager
from utils import validate_input

# Resumo do Desafio 16:
# O sistema permite gerenciar tarefas e integrá-las a um calendário, como o Google Calendar.


def main():
    task_manager = TaskManager()
    calendar_integration = CalendarIntegration()

    print("Bem-vindo ao Sistema de Gerenciamento de Tarefas e Calendário!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar nova tarefa")
        print("2. Remover tarefa")
        print("3. Listar tarefas")
        print("4. Integrar tarefa ao calendário")
        print("5. Sair")

        option = validate_input("Opção: ", int)

        if option == 1:
            title = input("Título da tarefa: ")
            description = input("Descrição: ")
            date = input("Data da tarefa (AAAA-MM-DD): ")
            task_manager.add_task(title, description, date)
        elif option == 2:
            task_id = validate_input("ID da tarefa para remover: ", int)
            task_manager.remove_task(task_id)
        elif option == 3:
            task_manager.list_tasks()
        elif option == 4:
            task_id = validate_input(
                "ID da tarefa para integrar ao calendário: ", int)
            calendar_integration.integrate_task(task_manager.get_task(task_id))
        elif option == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script gerencia a interação com o usuário para manipulação de tarefas e integração com um calendário.
# A separação de responsabilidades foi feita entre o módulo de tarefas e o de integração de calendário para garantir clareza no código.
