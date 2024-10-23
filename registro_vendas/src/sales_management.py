class SalesManager:
    def __init__(self):
        """
        Inicializa o gerenciador de vendas com uma lista vazia de vendas.
        """
        self.sales = []

    def register_sale(self, product_name, amount, price_per_unit):
        """
        Registra uma nova venda.

        :param product_name: Nome do produto vendido.
        :param amount: Quantidade vendida.
        :param price_per_unit: Preço por unidade.
        """
        sale = {
            "product_name": product_name,
            "amount": amount,
            "price_per_unit": price_per_unit,
            "total_value": amount * price_per_unit
        }
        self.sales.append(sale)
        print(
            f"Venda de {amount} unidades de '{product_name}' registrada com sucesso.")

    def get_sales_data(self):
        """
        Retorna todos os dados de vendas registrados.

        :return: Lista de vendas.
        """
        return self.sales
