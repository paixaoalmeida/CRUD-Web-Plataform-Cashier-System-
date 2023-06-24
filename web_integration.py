from flask import Flask
from flask import render_template
from flask import url_for
from src.database.database import *

db = Database()
web = Flask(__name__)

db.connect_to_database()
#Always initialize connection to have the cursor attribute


@web.route("/")
def hello():
    url_for('static', filename='style.css')
    return render_template('page.html')


@web.route("/produtos")
def show_produtos_get():
    products = db.show_all_products()
    return render_template('produtos.html', products=products)
