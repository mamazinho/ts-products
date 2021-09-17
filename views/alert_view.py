from controllers.product_controller import ProductController


class Alert:

    # Alerta que o estoque está zerado / info importante p/ catalogo
    def alert_stock(self):
        stocks = ProductController().read_all_products()
        for stock in stocks:
            if stock.actual_stock:
                print(f'stock: ', stock.actual_stock)
            else:
                print(f'stock zerado chamar outra eleição!!', stock.actual_stock)
            # aqui sera chamado catolog para realizar outra eleição!!

    # Faz o alerta do menor preço
    def alert_lower_price(self):
        prices = []
        lower_price = []
        prices = ProductController().read_all_products()
        for i in prices:
            lower_price.append(min([i.actual_price]))
            print(f'Menor preço!!', lower_price)
        return print(f'# aqui sera chamado catolog para realizar outra eleição!!', min(lower_price))

    # Alerta qual o menor preço entre os produtos que tem o mesmo GTIN
    def alert_lower_price_by_gtin(self):
        products = ProductController().read_by_gtin("teste gtin")
        prods = []
        for prod in products:
            prods.append(prod.actual_price)
        minor_price = min(prods)

        for prod_id in products:
            if prod_id.actual_price == minor_price:
                prod_minor_id = prod_id.id

        return prod_minor_id
