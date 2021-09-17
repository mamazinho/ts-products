from config.database import Database
from models.product_price_model import ProductPriceModel


class ProductPriceDao:

    def __init__(self, product_price: dict = {}):
        self.product_price = product_price

    def create(self):
        with Database() as session:
            product_price = ProductPriceModel(
                product_id=self.product_price['product_id'], price=self.product_price['price'])
            session.add(product_price)
            session.flush()
            session.commit()
            return product_price.id

    def read_all(self):
        with Database() as session:
            products_price = session.query(ProductPriceModel).all()
            return products_price

    def read_by_product_id(self):
        with Database() as session:
            product_price = session.query(ProductPriceModel).filter_by(
                product_id=self.product_price['product_id']).all()
            return product_price

    def read_by_id(self):
        with Database() as session:
            product_price = session.query(ProductPriceModel).get(self.product_price['product_id'])
            return product_price

    def update(self):
        with Database() as session:
            price_update = session.query(ProductPriceModel).filter_by(id=self.product_price['product_id'])
            price_update.update({
                "price": self.product_price['price'] if self.product_price['price'] else price_update[0].price,
            })
            session.commit()
