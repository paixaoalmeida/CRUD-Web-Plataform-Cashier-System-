import psycopg2
from src.database.database import *


# Storing the class into a object
database = Database()


class Produto():
    """
    This class gets methods from the Database module

    It's a class to do stuff related to the products and related

    For every method, we use the database.connect_to_database to
    connect to the database and right below, the methode
    """

    def __init__(self):
        pass

    def add_product(self):
        database.connect_to_database()
        database.add_product_and_query()

    def show_products(self):
        database.connect_to_database()
        database.show_all_products()

    def remove_product(self):
        database.connect_to_database()
        database.remove_products()


class RegisterProduct(Database):
    """
    Had to create another class in the file (but it's related to product)

    Here we use this Child Class of the Database class and register a purchase
    """
    def __init__(self):
        super().__init__()
        self.connect_to_database()

    @classmethod
    def register_purchase(cls):
        """
        In this methode we also use the attributes of the Database class to make and
        math operation into the database (take one item out of one product if something is bought)

        It's the same thing as the pegar_nomes() method of functions_system does

        U can see that we stored the cls parameter in the 'instance' variable.
        If i don't do that,thu database proporties are not gonna be recognized in this
        method, because the @classmethod refers to class itself, so we cannot use 'self.cursor'

        Insted, we use the cls.cursor, because the cls parameter refers to the class, and it does
        have the properties of Database
        """
        instance = cls()

        data_list = []  # LIsta vazia que vai pegar os valores
        arg = {'ID do produto:': int, 'Quantidade comprada:': int,
               'Valor da compra:': float,
               'Nome do cliente:': str}

        for nome, tipo in arg.items():
            quest = tipo(input(f'Digite {nome} '))
            data_list.append(quest)

        try:
            instance.cursor.execute('''
                UPDATE produtos
                set quantidade_produto = quantidade_produto - %s
                where id_product = %s
            ''', (data_list[1], data_list[0]))
            instance.connection.commit()
            instance.connection.close()

        except psycopg2.Error as erro_db:
            print(f'Erro {erro_db}')
