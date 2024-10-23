from project_management import ProjectManager
from time_tracking import TimeTracker
from utils import validate_input

# Resumo do Desafio 17:
# Este sistema permite gerenciar projetos, acompanhando seu progresso e rastreando o tempo gasto em cada um deles.


def main():
    project_manager = ProjectManager()
    time_tracker = TimeTracker()

    print("Bem-vindo ao Sistema de Gestão de Projetos!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Criar novo projeto")
        print("2. Atualizar projeto")
        print("3. Listar projetos")
        print("4. Iniciar rastreamento de tempo")
        print("5. Parar rastreamento de tempo")
        print("6. Sair")

        option = validate_input("Opção: ", int)

        if option == 1:
            name = input("Nome do projeto: ")
            description = input("Descrição: ")
            deadline = input("Data de entrega (AAAA-MM-DD): ")
            project_manager.create_project(name, description, deadline)
        elif option == 2:
            project_id = validate_input("ID do projeto para atualizar: ", int)
            status = input("Novo status: ")
            project_manager.update_project_status(project_id, status)
        elif option == 3:
            project_manager.list_projects()
        elif option == 4:
            project_id = validate_input(
                "ID do projeto para iniciar rastreamento: ", int)
            time_tracker.start_tracking(project_id)
        elif option == 5:
            project_id = validate_input(
                "ID do projeto para parar rastreamento: ", int)
            time_tracker.stop_tracking(project_id)
        elif option == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script centraliza a lógica de interação com o usuário, permitindo criar, listar e monitorar projetos,
# além de iniciar/parar o rastreamento de tempo. A separação entre as responsabilidades de gestão de projetos e controle de tempo
# ajuda na organização e manutenção do código.
