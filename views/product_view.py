from controllers.product_controller import ProductController
from views.catalog_view import Catalog

# View de operações de CRUD simples da tabela Produto


class Product:
    def __init__(self):
        self.categories = [1]

    def create_product(self):
        gtin = 'teste gtin'
        print("Consultando catalog com o gtin: ", gtin)
        product_catalog = Catalog().consult_gtin(gtin)
        if product_catalog is not None:
            print('Criando o produto com dados de catalog...')
            id = ProductController().create_product(product_catalog[1], product_catalog[3], product_catalog[5], 'moderation',
                                                    25, 10, 10, 'teste gtin', True, self.categories)
            self.product_id = id
            product_measures = ProductController().create_product_measures(15, 23, 26, 2.000, id)
            self.product_measures_id = product_measures
            election = Catalog().generate_election(id)
            print("Criado Produto com id:", id,
                  "e as medidas com id:", product_measures)
        else:
            print('Criando o produto com dados do seller...')
            id = ProductController().create_product('teste prod', 'teste desc', 'Marca', 'moderation',
                                                    99, 10, 10, 'teste gtin', True, self.categories)
            self.product_id = id
            product_measures = ProductController().create_product_measures(15, 23, 26, 2.000, id)
            self.product_measures_id = product_measures
            election = Catalog().generate_election(id)
            print("Criado Produto com id:", id,
                  "e as medidas com id:", product_measures)

    def read_all_products(self):
        products = ProductController().read_all_products()
        for prod in products:
            print(prod)

    def update_product(self):
        ProductController().update_product(self.product_id, actual_price=12)
        election = Catalog().generate_election(id)

    def delete_product(self):
        product = ProductController().delete_product(self.product_id)
