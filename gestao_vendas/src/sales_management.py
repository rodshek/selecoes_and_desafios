class SalesManager:
    def __init__(self):
        """
        Inicializa o gerenciador de vendas com uma lista vazia.
        """
        self.sales = []

    def register_sale(self, product, quantity, price):
        """
        Registra uma nova venda.

        :param product: Nome do produto.
        :param quantity: Quantidade vendida.
        :param price: Preço unitário.
        """
        sale = {
            "product": product,
            "quantity": quantity,
            "total_price": quantity * price
        }
        self.sales.append(sale)
        print(
            f"Venda registrada: {product} | Quantidade: {quantity} | Total: R${sale['total_price']:.2f}")

    def list_sales(self):
        """
        Lista todas as vendas registradas.
        """
        if not self.sales:
            print("Nenhuma venda registrada.")
            return

        print("\nVendas Registradas:")
        for idx, sale in enumerate(self.sales, 1):
            print(
                f"{idx}. Produto: {sale['product']}, Quantidade: {sale['quantity']}, Total: R${sale['total_price']:.2f}")
