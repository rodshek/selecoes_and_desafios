from report_generator import ReportGenerator
from sales_management import SalesManager
from utils import validate_input


def main():
    sales_manager = SalesManager()
    report_generator = ReportGenerator()

    print("Bem-vindo ao Sistema de Registro de Vendas!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Registrar uma nova venda")
        print("2. Gerar relatório mensal")
        print("3. Sair")

        option = validate_input("Opção: ", int)

        if option == 1:
            product = input("Nome do produto: ")
            amount = validate_input("Quantidade vendida: ", int)
            price = validate_input("Preço por unidade: ", float)
            sales_manager.register_sale(product, amount, price)
        elif option == 2:
            month = validate_input("Mês para o relatório (1-12): ", int)
            year = validate_input("Ano para o relatório (YYYY): ", int)
            report_generator.generate_report(
                sales_manager.get_sales_data(), month, year)
        elif option == 3:
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

# Explicação:
# Este script centraliza a interação com o usuário para registrar vendas e gerar relatórios mensais
# com base nos dados registrados.
