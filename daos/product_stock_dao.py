from config.database import Database
from models.product_stock_model import ProductStockModel


class ProductStockDao:

    def __init__(self, product_stock: dict = {}):
        self.product_stock = product_stock

    def create(self):
        with Database() as session:
            product_stock = ProductStockModel(
                product_id=self.product_stock['product_id'], stock=self.product_stock['stock'])
            session.add(product_stock)
            session.flush()
            session.commit()
            return product_stock.id

    def read_all(self):
        with Database() as session:
            products_stock = session.query(ProductStockModel).all()
            return products_stock

    def read_by_product_id(self):
        with Database() as session:
            product_stock = session.query(ProductStockModel).filter_by(product_id=self.product_stock['product_id'])
            return product_stock

    def read_by_id(self):
        with Database() as session:
            product_stock = session.query(ProductStockModel).get(self.product_stock['product_id'])
            return product_stock

    def delete(self):
        with Database() as session:
            result = session.query(ProductStockModel).filter_by(id=self.product_stock['product_id']).delete()
            session.commit()

    def update(self):
        with Database() as session:
            stock_update = session.query(ProductStockModel).filter_by(id=self.product_stock['product_id'])
            stock_update.update({
                "stock": self.product_stock['stock'] if self.product_stock['stock'] else stock_update[0].stock,
            })
            session.commit()
