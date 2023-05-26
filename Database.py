import psycopg2

class Database:
    def __init__(self, connection=None):
        self.connection = connection

    def connect_to_database(self):
        self.connection = psycopg2.connect(database="postgres",
                                           host="localhost",
                                           user="postgres",
                                           password="teste",
                                           port="5432")
        self.cursor = self.connection.cursor()

    def show_all_tables(self):
        self.cursor.execute('''
            SELECT * FROM clientes
        ''')

