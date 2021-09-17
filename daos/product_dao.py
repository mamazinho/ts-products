from config.database import Database
from models.product_model import ProductModel
from models.product_measure_model import ProductMeasuresModel
from models.category_model import CategoryModel
from models.product_category_model import ProductCategoryModel
from datetime import datetime


class ProductDao:

    def __init__(self, product={}):
        self.product = product

    def create(self):
        with Database() as session:
            categories = self.__categories_object(session, self.product.get('categories'))

            product = ProductModel(
                seller_id=self.product['seller_id'],
                name=self.product['name'],
                description=self.product['description'],
                brand=self.product['brand'],
                status=self.product['status'],
                created_at=datetime.now(),
                actual_stock=self.product['actual_stock'],
                actual_price=self.product['actual_price'],
                gtin=self.product['gtin'],
                categories=categories
            )
            session.add(product)
            session.flush()
            session.commit()
            return product.id

    def create_product_measures(self):
        with Database() as session:
            product = ProductMeasuresModel(
                product_id=self.product['product_id'],
                width_value=self.product['width_value'],
                height_value=self.product['height_value'],
                length_value=self.product['length_value'],
                weight_value=self.product['weight_value']
            )
            session.add(product)
            session.flush()
            session.commit()
            return product.id

    def read(self):
        with Database() as session:
            products = session.query(ProductModel).filter_by(active=True).all()
            return products

    def read_by_id(self):
        with Database() as session:
            product = session.query(ProductModel).filter_by(id=self.product['id']).all()
            return product[0]

    def read_measures_id(self):
        with Database() as session:
            product = session.query(ProductMeasuresModel).filter_by(product_id=self.product['product_id']).all() 
            return product[0]

    def read_by_name(self):
        with Database() as session:
            product = session.query(ProductModel).filter(
                ProductModel.name.contains(self.product['name']),
                ProductModel.active == True).all()
            return product

    def read_by_gtin(self):
        with Database() as session:
            product = session.query(ProductModel).filter(
                ProductModel.gtin == self.product['gtin'],
                ProductModel.active == True).all()
            return product

    def read_by_seller_id(self):
        with Database() as session:
            product = session.query(ProductModel).filter(
                ProductModel.seller_id == self.product['seller_id'],
                ProductModel.active == True).all()
            return product

    def read_by_category_id(self):
        with Database() as session:
            products = []
            categories = self.__categories_object(session, self.product.get('categories'))
            list_products = session.query(ProductCategoryModel.table).filter_by(category_id = categories[0].id).all()
            for prod in list_products:
                product = session.query(ProductModel).filter_by(id=prod[0]).all()
                products.append(product[0])
            return products

    def update(self):
        if not 'id' in self.product or not self.product['id']:
            return self.create()

        with Database() as session:
            categories = self.__categories_object(session, self.product.get('categories'))
            the_product = session.query(ProductModel).filter_by(id=self.product['id'])

            the_product.update({
                'id': self.product['id'],
                'seller_id': self.product['seller_id'] if self.product['seller_id'] else the_product[0].seller_id,
                'name': self.product['name'] if self.product['name'] else the_product[0].name,
                'description': self.product['description'] if self.product['description'] else the_product[0].description,
                'created_at': datetime.now(),
                'actual_stock': self.product['actual_stock'] if self.product['actual_stock'] else the_product[0].actual_stock,
                'actual_price': self.product['actual_price'] if self.product['actual_price'] else the_product[0].actual_price,
                'gtin': self.product['gtin'] if self.product['gtin'] else the_product[0].gtin,
                'active': self.product['active'],
            })
            the_product = session.query(ProductModel).get(self.product['id'])
            if categories:
                the_product.categories[:] = []
                for cat in categories:
                    the_product.categories.append(cat)
            session.commit()

    def __categories_object(self, session, product_categories):
        categories = []

        if product_categories:
            for category_id in product_categories:
                category = session.query(CategoryModel).filter_by(id=category_id)
                categories.append(category[0])

        return categories
