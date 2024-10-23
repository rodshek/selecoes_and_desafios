import sys

from employee_database import EmployeeDatabase
from utils import validate_input

# Resumo do Desafio 4:
# Este script implementa um sistema básico de gerenciamento de funcionários usando um banco de dados SQLite.
# Ele permite adicionar, atualizar, remover e listar funcionários.


def main():
    db = EmployeeDatabase('database/funcionarios.db')
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar funcionário")
        print("2. Atualizar funcionário")
        print("3. Listar funcionários")
        print("4. Remover funcionário")
        print("5. Sair")

        choice = input("Opção: ")
        if choice == '1':
            nome = input("Nome do funcionário: ")
            idade = validate_input("Idade: ", int)
            cargo = input("Cargo: ")
            db.add_employee(nome, idade, cargo)
            print(f"Funcionário {nome} adicionado com sucesso.")
        elif choice == '2':
            id_funcionario = validate_input(
                "ID do funcionário para atualizar: ", int)
            nome = input("Novo nome: ")
            idade = validate_input("Nova idade: ", int)
            cargo = input("Novo cargo: ")
            db.update_employee(id_funcionario, nome, idade, cargo)
            print(f"Funcionário ID {id_funcionario} atualizado com sucesso.")
        elif choice == '3':
            print("\nLista de Funcionários:")
            employees = db.list_employees()
            for emp in employees:
                print(emp)
        elif choice == '4':
            id_funcionario = validate_input(
                "ID do funcionário para remover: ", int)
            db.remove_employee(id_funcionario)
            print(f"Funcionário ID {id_funcionario} removido.")
        elif choice == '5':
            print("Saindo...")
            sys.exit(0)
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# O script fornece um menu interativo para realizar operações no banco de dados. Ele interage diretamente com o módulo employee_database.py
# e usa funções auxiliares para validar as entradas.
