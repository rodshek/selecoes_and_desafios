from tabulate import tabulate


def generate_report(sales):
    """
    Gera um relatório detalhado de vendas.

    :param sales: Lista de vendas.
    """
    if not sales:
        print("Nenhuma venda disponível para gerar relatório.")
        return

    headers = ["Produto", "Quantidade", "Total (R$)"]
    table = [[sale["product"], sale["quantity"],
              f"R${sale['total_price']:.2f}"] for sale in sales]

    print("\nRelatório de Vendas:")
    print(tabulate(table, headers, tablefmt="grid"))
