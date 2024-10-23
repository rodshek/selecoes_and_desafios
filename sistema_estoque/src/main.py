from inventory_management import InventoryManagement
from utils import validate_input

# Resumo do Desafio 07:
# Este script permite gerenciar um sistema de estoque com opções para adicionar, remover e atualizar itens.


def main():
    inventory = InventoryManagement()

    while True:
        print("\nSistema de Estoque")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Atualizar quantidade")
        print("4. Listar estoque")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do item: ")
            quantity = validate_input("Quantidade inicial: ", int)
            inventory.add_item(name, quantity)
            print(f"Item '{name}' adicionado com sucesso.")
        elif choice == '2':
            item_id = validate_input("ID do item a ser removido: ", int)
            if inventory.remove_item(item_id):
                print("Item removido com sucesso.")
            else:
                print("Erro ao remover item. Verifique o ID.")
        elif choice == '3':
            item_id = validate_input("ID do item a ser atualizado: ", int)
            quantity = validate_input("Nova quantidade: ", int)
            if inventory.update_item_quantity(item_id, quantity):
                print("Quantidade atualizada com sucesso.")
            else:
                print("Erro ao atualizar quantidade. Verifique o ID.")
        elif choice == '4':
            items = inventory.list_items()
            print("\nEstoque Atual:")
            for item in items:
                print(
                    f"ID: {item['id']} | Item: {item['name']} | Quantidade: {item['quantity']}")
        elif choice == '5':
            print("Saindo do sistema de estoque.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script oferece uma interface para o gerenciamento do estoque. As funções interagem com o módulo
# inventory_management para realizar as operações de adição, remoção e atualização do estoque.
