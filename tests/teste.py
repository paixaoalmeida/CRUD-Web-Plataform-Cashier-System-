#The purpose of this file is to make some tests in the code when i need to.
import psycopg2
from database.Database import *
from res.functions_system import *



connection = psycopg2.connect(database="Sistema_caixa",
                                       host="localhost",
                                       user="postgres",
                                       password="teste",
                                       port="5432")
cursor = connection.cursor()


cursor.execute('''
    SELECT * FROM produtos
    ''')
all_itens = cursor.fetchall()
# Tupla dentro de uma lista

    # Dando um loop em todos os valores das tuplas retornadas
print(all_itens)

