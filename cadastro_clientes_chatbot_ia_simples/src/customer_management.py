class CustomerManager:
    def __init__(self):
        """
        Inicializa o gerenciador de clientes com uma lista vazia.
        """
        self.customers = []
        self.customer_id_counter = 1

    def add_customer(self, name, email, phone):
        """
        Adiciona um novo cliente à lista.

        :param name: Nome do cliente.
        :param email: E-mail do cliente.
        :param phone: Telefone do cliente.
        """
        customer = {
            "id": self.customer_id_counter,
            "name": name,
            "email": email,
            "phone": phone
        }
        self.customers.append(customer)
        self.customer_id_counter += 1
        print(f"Cliente '{name}' adicionado com sucesso!")

    def update_customer(self, customer_id, name=None, email=None, phone=None):
        """
        Atualiza as informações de um cliente existente.

        :param customer_id: ID do cliente.
        :param name: Novo nome do cliente (se fornecido).
        :param email: Novo e-mail do cliente (se fornecido).
        :param phone: Novo telefone do cliente (se fornecido).
        """
        for customer in self.customers:
            if customer["id"] == customer_id:
                if name:
                    customer["name"] = name
                if email:
                    customer["email"] = email
                if phone:
                    customer["phone"] = phone
                print(f"Cliente '{customer['name']}' atualizado com sucesso.")
                return
        print(f"Cliente com ID {customer_id} não encontrado.")

    def remove_customer(self, customer_id):
        """
        Remove um cliente da lista.

        :param customer_id: ID do cliente a ser removido.
        """
        for customer in self.customers:
            if customer["id"] == customer_id:
                self.customers.remove(customer)
                print(f"Cliente '{customer['name']}' removido com sucesso.")
                return
        print(f"Cliente com ID {customer_id} não encontrado.")

    def list_customers(self):
        """
        Lista todos os clientes cadastrados.
        """
        if not self.customers:
            print("Nenhum cliente cadastrado.")
        else:
            print("\nClientes Cadastrados:")
            for customer in self.customers:
                print(
                    f"ID: {customer['id']}, Nome: {customer['name']}, E-mail: {customer['email']}, Telefone: {customer['phone']}")
