from config.database import Database
from models.product_measure_model import ProductMeasuresModel


class ProductMeasuresDao:

    def __init__(self, product_measure: dict = {}):
        self.product_measure = product_measure

    def create(self):
        with Database() as session:
            product_measure = ProductMeasuresModel(
                product_id=self.product_measure['product_id'], 
                width_value=self.product_measure['width_value'], 
                height_value=self.product_measure['height_value'], 
                length_value=self.product_measure['length_value'], 
                weight_value=self.product_measure['weight_value'])
            session.add(product_measure)
            session.flush()
            session.commit()
            return product_measure.id

    def read_all(self):
        with Database() as session:
            product_measure = session.query(ProductMeasuresModel).all()
            return product_measure

    def read_by_product_id(self):
        with Database() as session:
            product_measure = session.query(ProductMeasuresModel).filter_by(
                product_id=self.product_measure['product_id']).all()
            return product_measure

    def read_by_id(self):
        with Database() as session:
            product_measure = session.query(ProductMeasuresModel).get(
                self.product_measure['product_id'])
            return product_measure

    def update(self):
        with Database() as session:
            measures_update = session.query(ProductMeasuresModel).filter_by(
                id=self.product_measure['product_id'])
            measures_update.update({
                "width_value": self.product_measure['width_value'] if self.product_measure['width_value'] else measures_update[0].width_value,
                "height_value": self.product_measure['height_value'] if self.product_measure['height_value'] else measures_update[0].height_value,
                "length_value": self.product_measure['length_value'] if self.product_measure['length_value'] else measures_update[0].length_value,
                "weight_value": self.product_measure['weight_value'] if self.product_measure['weight_value'] else measures_update[0].weight_value,
            })
            session.commit()
