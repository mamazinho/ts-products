from views.category_view import Category
from views.product_view import Product
from views.product_read_by_view import ReadByProduct
from views.historic_views import Historic
from views.product_update_view import UpdateProduct
from views.alert_view import Alert

class Main:

    def __init__(self):
        self.category = Category()
        self.product = Product()
        self.read_by_product = ReadByProduct()
        self.historic = Historic()
        self.update_product = UpdateProduct()
        self.alert = Alert()
      
    #  ---------------- CATEGORIAS ----------------
        self.category.create_category()
        self.category.read_all_categories()
        self.category.update_category()
        self.category.read_by_category_id()

    #  ----------------- PRODUTOS -----------------
        self.product.create_product()
        self.product.read_all_products()
        self.product.update_product()

    #  --------------- LEITURA DO PRODUTO POR ALGUMA COISA ----------
        self.read_by_product.read_product_by_id()
        self.read_by_product.read_measures_id()
        self.read_by_product.read_product_by_name()
        self.read_by_product.read_product_by_category()
        self.read_by_product.read_product_by_gtin()
        self.read_by_product.read_product_by_seller_id()

    #  --------------- CRIAÇAO E LEITURA DE HISTÓRICO DO PRODUTO E ESTOQUE -------
        self.historic.read_all_product_price()
        self.historic.read_all_product_stock()
        self.historic.create_product_price()
        self.historic.create_product_stock()

    # --------------- ATUALIZAÇÃO DE ITENS DO PRODUTO -------------------
        self.update_product.update_product_price()
        self.update_product.update_product_stock()
        self.update_product.update_lower_price()
        self.update_product.update_stock()

    # ---------------- ALERTAS IMPORTANTES P/ O NEGOCIO -----------------
        self.alert.alert_stock()
        self.alert.alert_lower_price()
        self.alert.alert_lower_price_by_gtin()

Main()
