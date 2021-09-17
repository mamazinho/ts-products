from controllers.product_controller import ProductController


class ReadByProduct:

    def __init__(self):
        self.product_id = 1
        self.categories = [1]

    # Lendo as informações de um produto por ID
    def read_product_by_id(self):
        product = ProductController().read_by_id(self.product_id)
        print(product)

    # Lendo as medidas de determinado produto pelo seu ID
    def read_measures_id(self):
        product_mearure = ProductController().read_measures_id(self.product_id)
        print(product_mearure)

    # Lendo um ou mais produtos pelo seu nome
    def read_product_by_name(self):
        products = ProductController().read_by_name('name_catalog')
        for prod in products:
            print(prod)

    # Lendo todos os produtos ativos que estão em uma determinada categoria
    def read_product_by_category(self):
        products = ProductController().read_by_category_id(self.categories)
        for prod in products:
            print(f'Produto de categoria: ', prod)

    # Lendo todos os produtos que tem o mesmo GTIN
    def read_product_by_gtin(self):
        products = ProductController().read_by_gtin('teste gtin')
        for prod in products:
            print(prod)

    # Lendo todos os produtos de um determinado seller, pelo seller ID
    def read_product_by_seller_id(self):
        products = ProductController().read_by_seller_id(25)
        for prod in products:
            print(prod)
