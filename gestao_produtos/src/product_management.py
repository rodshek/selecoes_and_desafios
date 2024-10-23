class ProductManagement:
    def __init__(self):
        """
        Inicializa o sistema de gestão de produtos com um dicionário de produtos.
        """
        self.products = {}
        self.next_id = 1

    def add_product(self, name, price, quantity):
        """
        Adiciona um novo produto ao inventário.

        :param name: Nome do produto.
        :param price: Preço do produto.
        :param quantity: Quantidade do produto em estoque.
        """
        product = {
            "id": self.next_id,
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products[self.next_id] = product
        self.next_id += 1

    def update_product(self, product_id, name=None, price=None, quantity=None):
        """
        Atualiza as informações de um produto.

        :param product_id: ID do produto a ser atualizado.
        :param name: Novo nome do produto (opcional).
        :param price: Novo preço do produto (opcional).
        :param quantity: Nova quantidade do produto (opcional).
        :return: True se o produto foi atualizado com sucesso, False se o produto não for encontrado.
        """
        if product_id in self.products:
            if name:
                self.products[product_id]['name'] = name
            if price is not None:
                self.products[product_id]['price'] = price
            if quantity is not None:
                self.products[product_id]['quantity'] = quantity
            return True
        return False

    def remove_product(self, product_id):
        """
        Remove um produto do inventário.

        :param product_id: ID do produto a ser removido.
        :return: True se o produto foi removido, False se o produto não for encontrado.
        """
        return self.products.pop(product_id, None) is not None

    def list_products(self):
        """
        Lista todos os produtos no inventário.

        :return: Uma lista de dicionários representando os produtos.
        """
        return list(self.products.values())
