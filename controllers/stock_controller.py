from daos.product_stock_dao import ProductStockDao


class StockController():

    def create_stock(self, product_id, stock):
        new_stock = {
            "product_id": product_id,
            "stock": stock
        }
        stock_id = ProductStockDao(new_stock).create()
        return stock_id

    def read_all_stocks(self):
        list_stocks = ProductStockDao().read_all()
        return list_stocks

    def read_by_stock_id(self, product_id, stock):
        product_id = {
            'id': product_id,
            'stock': stock
        }
        list_stock = ProductStockDao(product_id).read_by_id()
        return list_stock

    def delete_stock(self, stock_id):
        stock = {
            "id": stock_id
        }
        ProductStockDao(stock).delete()

    def update_stock(self, id, product_id, stock):
        stock_update = {
            "id": id,
            "product_id": product_id,
            "stock": stock
        }
        ProductStockDao(stock_update).update()
