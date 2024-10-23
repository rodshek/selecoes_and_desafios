from tabulate import tabulate


class InventoryManager:
    def __init__(self):
        """
        Inicializa o gerenciador de estoque com um dicionário vazio.
        """
        self.inventory = {}

    def add_product(self, name, quantity, price):
        """
        Adiciona um novo produto ao estoque.

        :param name: Nome do produto.
        :param quantity: Quantidade inicial.
        :param price: Preço unitário do produto.
        """
        if name in self.inventory:
            print(
                f"O produto '{name}' já existe no estoque. Atualize a quantidade ou o preço se necessário.")
        else:
            self.inventory[name] = {"quantity": quantity, "price": price}
            print(f"Produto '{name}' adicionado ao estoque.")

    def update_quantity(self, name, quantity):
        """
        Atualiza a quantidade de um produto no estoque.

        :param name: Nome do produto.
        :param quantity: Nova quantidade.
        """
        if name in self.inventory:
            self.inventory[name]["quantity"] = quantity
            print(
                f"Quantidade do produto '{name}' atualizada para {quantity}.")
        else:
            print(f"O produto '{name}' não foi encontrado no estoque.")

    def view_inventory(self):
        """
        Exibe o estoque atual em formato de tabela.
        """
        if not self.inventory:
            print("O estoque está vazio.")
            return

        headers = ["Produto", "Quantidade",
                   "Preço Unitário (R$)", "Total (R$)"]
        table = []
        for name, details in self.inventory.items():
            total_value = details["quantity"] * details["price"]
            table.append([name, details["quantity"],
                         f"R${details['price']:.2f}", f"R${total_value:.2f}"])

        print("\nEstoque Atual:")
        print(tabulate(table, headers, tablefmt="grid"))
