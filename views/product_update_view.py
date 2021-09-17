from controllers.product_controller import ProductController
from controllers.stock_controller import StockController
from controllers.price_controller import PriceController

from views.catalog_view import Catalog


class UpdateProduct:
    def __init__(self):
        self.product_id = 1
        self.price_id = 1
        self.stock_id = 1

    # Atualiza o preço de um determinado produto pelo seu id
    def update_product_price(self):
        ProductController().update_product(self.product_id, actual_price=3333)
        election = Catalog().generate_election(id)

    # Atualiza o estoque de um determinado produto pelo seu id
    def update_product_stock(self):
        ProductController().update_product(self.product_id, actual_stock=3333)

    # ?? (primeiro grupo)
    def update_lower_price(self):
        print(self.product_id)
        prices = PriceController().read_all_prices()
        for price in prices:
            print(price)
            if self.product_id == 1 and self.product_id == self.product_id and self.price_id == self.price_id:
                PriceController().update_price(self.price_id, self.product_id, price=55.55)
                election = Catalog().generate_election(id)
        print(price)

    # ?? (primeiro grupo)
    def update_stock(self):
        print(self.product_id)
        stocks = StockController().read_all_stocks()
        for stock in stocks:
            print(stock)
            if self.product_id == 1 and self.product_id == self.product_id and self.price_id == self.price_id:
                StockController().update_stock(self.stock_id, self.product_id, stock=555.5)
        print(stock)
