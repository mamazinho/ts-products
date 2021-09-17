
# View que simula algumas funções que catálogo deve enviar para produto;
# No momento do cadastro de um produto, product verifica com o catálogo se esse gtin já existe,
# Se existir retorna os dados fixos daquele gtin;

class Catalog:
    def consult_gtin(self, gtin):
        ean = gtin
        if ean == 'teste gtin':
            product_catalog = [
                'name', 'name_catalog',
                'description', 'description catalog',
                'brand', 'brand_catalog',
            ]
            return product_catalog
        else:
            return None

    def generate_election(self, product_id):
        election = product_id
