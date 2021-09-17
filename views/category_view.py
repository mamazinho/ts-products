from controllers.category_controller import CategoryController

# CRUD básico da tabela Categoria


class Category:
    def __init__(self):
        self.categories = []
        self.categories_id = 0

    def create_category(self):
        id = CategoryController().create_category('teste cat', 'teste desc')
        self.categories.append(id)

    def read_all_categories(self):
        list_categories = CategoryController().read_all_categories()
        for cat in list_categories:
            self.categories_id = cat.id
            print(cat)

    def read_by_category_id(self):
        category = CategoryController().read_by_category_id(self.categories_id)
        print(category)

    def update_category(self):
        CategoryController().update_category(self.categories_id,
                                             'teste cat helena up', 'teste cat desc update')

    def delete_category(self):
        CategoryController().delete_category(self.categories_id)
