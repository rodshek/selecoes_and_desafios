from inventory_management import InventoryManager
from utils import validate_input

# Resumo do Desafio 15:
# O sistema de controle de estoque permite que o usuário adicione, atualize e visualize produtos no estoque.


def main():
    inventory_manager = InventoryManager()

    print("Bem-vindo ao Sistema de Controle de Estoque!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar novo produto")
        print("2. Atualizar quantidade de produto")
        print("3. Visualizar estoque")
        print("4. Sair")

        option = validate_input("Opção: ", int)

        if option == 1:
            name = input("Nome do produto: ")
            quantity = validate_input("Quantidade: ", int)
            price = validate_input("Preço unitário: ", float)
            inventory_manager.add_product(name, quantity, price)
        elif option == 2:
            name = input("Nome do produto: ")
            quantity = validate_input("Nova quantidade: ", int)
            inventory_manager.update_quantity(name, quantity)
        elif option == 3:
            inventory_manager.view_inventory()
        elif option == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# O script principal controla as interações com o usuário, permitindo adicionar produtos, atualizar quantidades e visualizar o estoque.
# A lógica principal de gerenciamento de estoque está separada no módulo `inventory_management` para facilitar a organização.
