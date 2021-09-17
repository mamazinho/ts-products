from daos.product_price_dao import ProductPriceDao


class PriceController():

    def criate_price(self, product_id, price):
        new_price = {
            "product_id": product_id,
            "price": price
        }
        price_id = ProductPriceDao(new_price).create()
        return price_id

    def read_all_prices(self):
        list_prices = ProductPriceDao().read_all()
        return list_prices

    def read_by_price_id(self, price_id):
        price_id = {
            'id': price_id
        }
        price = ProductPriceDao(price_id).read_by_id()
        return price

    def update_price(self, price_id, product_id, price):
        price_update = {
            "id": price_id,
            "product_id": product_id,
            "price": price
        }
        ProductPriceDao(price_update).update()
