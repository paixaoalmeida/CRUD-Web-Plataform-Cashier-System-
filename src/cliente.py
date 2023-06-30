from src.database.database import *


class Cliente(Database):
    """
    This Cliente class was created to do all the stuff related to clients in
    the program

    It's a child class and it does have all the attributes of the Database class
    (in the /database/database.py)
    """
    def __init__(self):
        """
        This function uses the INSERTO INTO method in SQL to add a cliente to
        the database

        It takes the self.cursor object from the Database class and gives the values:
        -Name of the cliente
        -CPF (ID in Brazil) of the client

        We se the %s method (borrow from C) to pass the values to the query

        And why do we do that?

        Because the values to the query go into a tuple insed another tuple
        (the SystemFunction.pegar_nomes() function return the indexes of this
        tuples
        
        Int the end, we do commit the change to the database and close the session
        """
        super().__init__()
        self.connect_to_database()

    def add_client(self, nome_cliente, cpf_cliente):
        try:
            self.cursor.execute('''
                INSERT INTO clientes(nome_cliente,cpf_cliente)
                VALUES(%s,%s);
                ''', (
                    nome_cliente, cpf_cliente))
            self.connection.commit()
    
        except psycopg2.Error as erro:
            print(f'{erro}')
            exit(1)



