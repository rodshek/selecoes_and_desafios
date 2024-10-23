from reports import generate_report
from sales_management import SalesManager
from utils import validate_input

# Resumo do Desafio 14:
# Este script implementa um sistema básico de gerenciamento de vendas que permite registrar, visualizar
# e gerar relatórios de vendas.


def main():
    sales_manager = SalesManager()

    print("Bem-vindo ao Sistema de Gestão de Vendas!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Registrar nova venda")
        print("2. Listar todas as vendas")
        print("3. Gerar relatório de vendas")
        print("4. Sair")

        option = validate_input("Opção: ", int)

        if option == 1:
            product = input("Produto: ")
            quantity = validate_input("Quantidade: ", int)
            price = validate_input("Preço unitário: ", float)
            sales_manager.register_sale(product, quantity, price)
        elif option == 2:
            sales_manager.list_sales()
        elif option == 3:
            generate_report(sales_manager.sales)
        elif option == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# O script principal lida com as interações do usuário, permitindo registrar vendas, visualizar as vendas
# registradas e gerar relatórios a partir delas. As funções principais de gerenciamento de vendas estão
# separadas em um módulo específico para facilitar a organização do código.
