import psycopg2


class Database:
    """
    This whole module and its classes and methods are designed just to
    interact with the PostGreeSQL database

    "Here we use the psycopg2 library to do that, currently we have the methods:
        -def connect_to_database
        -def show_all_products
        -def remove_products
        def add_product_and_query
    """

    def __init__(self, connection=None):
        self.connection = connection

    def connect_to_database(self):
        self.connection = psycopg2.connect(database="Sistema_caixa",
                                           host="localhost",
                                           user="postgres",
                                           password="teste",
                                           port="5432")
        self.cursor = self.connection.cursor()

    def show_all_products(self):
        """
        This function shows all the products listed in the 'products'
        table in the Database

        Pay attention, we take the function fetchall from psycopg2 and put it
        into the 'all_itens' variable' and then we loop over this variable
        using 'items'

        The reason we do this is because the result from the library is a tuple
        inside another tuple, so we use indexes to get the result out and format it
        to the user

        Note: No need to commit here because there is no need, we are just
        visualizing some data from the database

        In the end of the loop of the results of the database, we append the results
        in a list called produtos_list, this way we can return some data to the front-end
        server Flask
        """
        global produtos_list
        try:
            self.cursor.execute('''
                SELECT * FROM produtos
            ''')
            all_itens = self.cursor.fetchall()
            # Tupla dentro de uma lista

            produtos_list = []

            # Dando um loop em todos os valores das tuplas retornadas
            for item in all_itens:
                produtos = [item[0], item[1], item[2], item[3]]
                produtos_list.append(produtos)

            return produtos_list

        except psycopg2.Error as error_db:
            print('Algo deu errado! Siga o erro do banco abaixo: \n')
            print(f'{error_db}\n')
            print(error_db.diag)

    def remove_products(self):
        """
        This function just does a basic delete operation to some products in the database

        Commits the changes in the end and closes the section

        Here we use and DELETE statement with a WHERE using the id of the product
        to delete some product from de database

        Note: That block was updated with a context manager 'with', this way we
        make sure the connection with the db is closed with no bug, and just need
        to add the connection.commit() method
        """
        try:
            delete_request = str(input('Qual produto você quer deletar? '))
            with self.cursor as query:
                query.execute(f'''
                DELETE
                FROM produtos
                WHERE id_product = '{delete_request}'
            ''')
            self.connection.commit()

        except psycopg2.Error as error_db:
            print('Algo deu errado! Siga o erro do banco abaixo: \n')
            print(f'{error_db}\n')
            print(error_db.diag)
            exit(1)

    def add_product_and_query(self,nome_produto, preco_produto, quantidade_produto):
        """
        Here, thats the same as the pegar_nomes() function from function_system

        It does take the user's input with a for loop iterating through a dict

        Then we just use the %s method (borrow from C) to put the indexes in the
        query

        Then we have the with statement as a context manager, this way we
        make sure the connection with the db is closed with no bug, and just need
        to add the connection.commit() method
        """
        try:
            with self.cursor as query:
                query.execute(f"""
                    INSERT INTO produtos (nome_produto,preco_produto,quantidade_produto)
                    VALUES(%s,%s,%s); 
                    """, (
                        nome_produto, preco_produto, quantidade_produto))
                self.connection.commit()
        except psycopg2.Error as erro_db:
            print('Algo deu errado! Siga o erro do banco abaixo: \n')
            print(f'{erro_db}\n')
            print(erro_db.diag)
            exit(1)


