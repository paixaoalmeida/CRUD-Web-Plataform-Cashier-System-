from flask import Flask
from flask import render_template
from flask import url_for
from src.sistema import *


web = Flask(__name__)


@web.route("/")
def hello():
    url_for('static', filename='style.css')
    return render_template('page.html')


@web.route("/produtos")
def show_produtos_get():
    return product.show_products()
