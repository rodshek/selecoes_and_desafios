from customer_management import CustomerManager
from utils import validate_input

# Resumo do Desafio 18:
# Este sistema permite cadastrar, atualizar, remover e listar clientes para uma melhor organização e gestão.


def main():
    customer_manager = CustomerManager()

    print("Bem-vindo ao Sistema de Cadastro de Clientes!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar novo cliente")
        print("2. Atualizar cliente")
        print("3. Remover cliente")
        print("4. Listar clientes")
        print("5. Sair")

        option = validate_input("Opção: ", int)

        if option == 1:
            name = input("Nome do cliente: ")
            email = input("E-mail do cliente: ")
            phone = input("Telefone do cliente: ")
            customer_manager.add_customer(name, email, phone)
        elif option == 2:
            customer_id = validate_input("ID do cliente para atualizar: ", int)
            name = input("Novo nome (deixe vazio para manter): ")
            email = input("Novo e-mail (deixe vazio para manter): ")
            phone = input("Novo telefone (deixe vazio para manter): ")
            customer_manager.update_customer(customer_id, name, email, phone)
        elif option == 3:
            customer_id = validate_input("ID do cliente para remover: ", int)
            customer_manager.remove_customer(customer_id)
        elif option == 4:
            customer_manager.list_customers()
        elif option == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script centraliza a lógica de interação com o usuário para permitir o gerenciamento de clientes,
# incluindo adição, remoção, atualização e listagem. O código é organizado de forma modular,
# com a lógica de gerenciamento isolada no módulo `customer_management`, facilitando a manutenção e testes.
