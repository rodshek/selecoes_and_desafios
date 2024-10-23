from product_management import ProductManagement
from utils import validate_input

# Resumo do Desafio 11:
# Este script oferece um sistema de gestão de produtos, permitindo adicionar, remover, atualizar e listar produtos
# em um inventário.


def main():
    manager = ProductManagement()

    while True:
        print("\nSistema de Gestão de Produtos")
        print("1. Adicionar produto")
        print("2. Atualizar produto")
        print("3. Remover produto")
        print("4. Listar produtos")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do produto: ")
            price = validate_input("Preço do produto: ", float)
            quantity = validate_input("Quantidade do produto: ", int)
            manager.add_product(name, price, quantity)
            print(f"Produto {name} adicionado com sucesso.")
        elif choice == '2':
            product_id = validate_input(
                "ID do produto a ser atualizado: ", int)
            name = input(
                "Novo nome do produto (deixe em branco para não alterar): ")
            price = validate_input(
                "Novo preço do produto (deixe em branco para não alterar): ", float, optional=True)
            quantity = validate_input(
                "Nova quantidade do produto (deixe em branco para não alterar): ", int, optional=True)
            updated = manager.update_product(product_id, name, price, quantity)
            if updated:
                print(f"Produto {product_id} atualizado com sucesso.")
            else:
                print(f"Produto {product_id} não encontrado.")
        elif choice == '3':
            product_id = validate_input("ID do produto a ser removido: ", int)
            removed = manager.remove_product(product_id)
            if removed:
                print(f"Produto {product_id} removido com sucesso.")
            else:
                print(f"Produto {product_id} não encontrado.")
        elif choice == '4':
            products = manager.list_products()
            print("\nLista de Produtos:")
            for product in products:
                print(
                    f"ID: {product['id']}, Nome: {product['name']}, Preço: {product['price']}, Quantidade: {product['quantity']}")
        elif choice == '5':
            print("Saindo do sistema de gestão de produtos.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script principal oferece uma interface simples para adicionar, atualizar, remover e listar produtos em
# um inventário. As operações CRUD são realizadas no módulo product_management.py.
