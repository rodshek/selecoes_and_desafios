class ReportGenerator:
    def generate_report(self, sales_data, month, year):
        """
        Gera um relatório de vendas mensais.

        :param sales_data: Lista de vendas registradas.
        :param month: Mês para o qual o relatório será gerado.
        :param year: Ano para o qual o relatório será gerado.
        """
        print(f"\nRelatório de Vendas para {month}/{year}")
        total_sales_value = 0

        for sale in sales_data:
            # Para simplificação, o mês e o ano seriam extraídos da data da venda
            # (aqui estamos assumindo que todos os dados são do mês especificado).
            total_sales_value += sale["total_value"]

            print(
                f"Produto: {sale['product_name']}, Quantidade: {sale['amount']}, Valor Total: R${sale['total_value']:.2f}")

        print(
            f"\nValor total de vendas em {month}/{year}: R${total_sales_value:.2f}")
