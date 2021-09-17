from flask import Flask, render_template
import sys
import os
sys.path.append(os.getcwd())
from controllers.category_controller import CategoryController
from controllers.price_controller import PriceController
from controllers.stock_controller import StockController
from controllers.product_controller import ProductController
from controllers.measures_controller import MeasuresController

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/categories")
def categories():
    categories = CategoryController().read_all_categories()
    return render_template('categories.html', title="Categories", model=categories)

@app.route("/productprice")
def productPrice():
    product_price = PriceController().read_all_prices()
    return render_template('product_price.html', title="Product Price", model=product_price)

@app.route("/productstock")
def productStock():
    product_stock = StockController().read_all_stocks()
    return render_template('product_stock.html', title="Product Stock", model=product_stock)

@app.route("/products")
def products():
    products = ProductController().read_all_products()
    return render_template('products.html', title="Products", model=products)

@app.route("/productsmeasures")
def products_measures():
    products_measures = MeasuresController().read_all_measures()
    return render_template('products_measures.html', title="Products Measures", model=products_measures)


app.run(debug=True)
