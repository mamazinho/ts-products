from controllers.product_controller import ProductController

# Classe que cria e le todo histórico de preços e estoque de produtos


class Historic:

    # Resgata todo histórico dos preços dos produtos cadastrados
    def read_all_product_price(self):
        prices = ProductController().read_all_product_price()
        for price in prices:
            print(price)

    # Resgata todo histórico do estoque dos produtos cadastrados
    def read_all_product_stock(self):
        stocks = ProductController().read_all_product_stock()
        for stock in stocks:
            print(stock)

    # Cria o histórico de preços de um produto
    def create_product_price(self):
        id = ProductController().create_product_price(1, 10)
        self.price_id = id

    # Cria o histórico de estoque de um produto

    def create_product_stock(self):
        id = ProductController().create_product_stock(1, 10)
        self.stock_id = id
