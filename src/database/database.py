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
        """
        try:
            self.cursor.execute('''
                SELECT * FROM produtos
            ''')
            all_itens = self.cursor.fetchall()
            #Tupla dentro de uma lista

            # Dando um loop em todos os valores das tuplas retornadas
            for item in all_itens:
                print(f'''
                        nome: {item[0]}
                        preço: R${item[1]}
                        quantidade: {item[2]}
                        id: {item[3]}
                    ''')
        except psycopg2.Error as error_db:
            print('Algo deu errado! Siga o erro do banco abaixo: \n')
            print(f'{error_db}\n')
            print(error_db.diag)

    def remove_products(self):
        """
        This function just does a basic delete operation to some products in the database

        Commits the changes in the end and closes the section

        Here we can use and F string and just take the user's input
        and query
        """
        try:
            delete_request = str(input('Qual produto você quer deletar? '))
            self.cursor.execute(f'''
                DELETE
                FROM produtos
                WHERE nome_produto ILIKE '{delete_request}'
            ''')
            self.connection.commit()
            self.connection.close()

        except psycopg2.Error as error_db:
            print('Algo deu errado! Siga o erro do banco abaixo: \n')
            print(f'{error_db}\n')
            print(error_db.diag)
            exit(1)

    def add_product_and_query(self):
        """
        Here, thats the same as the pegar_nomes() function from function_system

        It does take the user's input with a for loop iterating through a dict

        Then we just use the %s method (borrow from C) to put the indexes in the
        query
        """
        prod_list = []
        arg = {'nome do produto:': str, 'preço do produto:': float, 'a quantidade:': int}

        for nome, tipo in arg.items():
            quest = tipo(input(f'Digite {nome} '))
            prod_list.append(quest)

        try:
            self.cursor.execute(f"""
                INSERT INTO produtos (nome_produto,preco_produto,quantidade_produto)
                VALUES(%s,%s,%s); 
                """, (
                prod_list[0], prod_list[1], prod_list[2]))  # Usando a função %s para definir uma váriavel - função do C
            self.connection.commit()  # Comitar as mudanças no banco
            self.connection.close()

        except psycopg2.Error as erro_db:
            print('Algo deu errado! Siga o erro do banco abaixo: \n')
            print(f'{erro_db}\n')
            print(erro_db.diag)
            exit(1)
        
