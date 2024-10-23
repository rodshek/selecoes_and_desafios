from task_manager import TaskManager
from utils import validate_input

# Resumo do Desafio 13:
# Este script permite ao usuário gerenciar uma lista de tarefas, oferecendo opções para adicionar,
# editar, remover e listar tarefas, além de marcar tarefas como concluídas e definir prioridades.


def main():
    task_manager = TaskManager()

    print("Bem-vindo ao Gerenciador de Tarefas!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Editar tarefa")
        print("4. Remover tarefa")
        print("5. Marcar tarefa como concluída")
        print("6. Sair")

        option = validate_input("Opção: ", int)

        if option == 1:
            title = input("Título da tarefa: ")
            priority = validate_input("Prioridade (1 a 5): ", int)
            task_manager.add_task(title, priority)
        elif option == 2:
            task_manager.list_tasks()
        elif option == 3:
            task_id = validate_input("ID da tarefa a editar: ", int)
            title = input("Novo título: ")
            priority = validate_input("Nova prioridade (1 a 5): ", int)
            task_manager.edit_task(task_id, title, priority)
        elif option == 4:
            task_id = validate_input("ID da tarefa a remover: ", int)
            task_manager.remove_task(task_id)
        elif option == 5:
            task_id = validate_input(
                "ID da tarefa a marcar como concluída: ", int)
            task_manager.mark_task_completed(task_id)
        elif option == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script implementa uma interface de linha de comando simples para que o usuário possa interagir com o sistema
# de gerenciamento de tarefas. As funções são organizadas no módulo TaskManager, e a validação de entrada é tratada
# pela função auxiliar validate_input.
