from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import abort
from src.database.database import *
from src.cliente import *

db = Database()
'''Initializing the Database module to use it
in the code'''

client = Cliente()

web = Flask(__name__)
'''Initializing Flask app in a object, so we can use it 
in the code'''

db.connect_to_database()
'''We need to call this methode before running other stuff
because most of the functions in the Database module use the
self.cursor attribute, and this attribute is just initialized
once we call this method'''


@web.route("/")
def main_page():
    """Main page of the system, here we declare the css stylesheet
    and return the page.html template"""

    url_for('static', filename='style.css')
    return render_template('page.html')


@web.route("/produtos")
def show_produtos_get():
    """Here we show all the products that are available in the database
    we put the show_all_products in the *products* object and return it
    when we declare the produtos.html template so we can use it in the
    teplate with jinja2 template language"""

    products = db.show_all_products()
    return render_template('produtos.html', products=products)


@web.route("/registro", methods=['POST', 'GET'])
def registro_cliente():
    if request.method == 'POST':
        cliente = request.form['nome_cliente']
        cpf = request.form['cpf_cliente']
        client.add_client(cliente, cpf)
        return render_template('sucesso_cadastro.html', cliente=cliente)
    else:
        return render_template('Registro_cliente.html')


