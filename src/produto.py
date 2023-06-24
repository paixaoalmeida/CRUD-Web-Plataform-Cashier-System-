import psycopg2
from src.database.database import *


# Storing the class into a object
database = Database()


class Produto:
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

    #MUDAR PARA REGISTRAR QUANTIDADE
    @classmethod
    def register_quantity_purchase(cls):
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
        arg = {'ID do produto:': int, 'Quantidade comprada:': int}

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

            return data_list[0]

        except psycopg2.Error as erro_db:
            print(f'Erro {erro_db}')

    @classmethod
    def register_data_of_purchase(cls):
        """
        Thin function is supposed to do a query to the database and
        register some customer's purchase by:

            -Add name of the client to the registro table
            -Add exact hour of the purchase
            -Value of the purchase ($$)
            -Name of the product

        It's a big query, it takes the ID of the product, analyse the produto
        table and replace the nome_produto column of registro table with
        the name of the product (By ID of the produto table)

        We declare a variable called NomePro in the query, so we can pass it
        to the VALUES camp and get the name of the product to be replaced
        """
        instance = cls()
        class_instance = RegisterProduct()

        client_info = []  # LIsta vazia que vai pegar os valores
        arg = {'Nome do cliente:': str, 'Valor da compra': float}

        for nome, tipo in arg.items():
            quest = tipo(input(f'Digite {nome} '))
            client_info.append(quest)

        instance.cursor.execute("""
            DO $$
                DECLARE NomePro varchar(15);
                BEGIN
	                SELECT nome_produto INTO NomePro FROM produtos
	                WHERE id_product = %s;
	
	            INSERT INTO registro(nome_produto,nome_cliente, valor_compra, data_compra)
	            VALUES(NomePro,%s,%s,now());
            END $$;

        """, (class_instance.register_quantity_purchase(), client_info[0], client_info[1],))

        instance.connection.commit()
        instance.connection.close()
