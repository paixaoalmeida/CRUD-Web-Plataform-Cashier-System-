#The purpose of this file is to make some tests in the code when i need to.
import psycopg2

#from res.functions_system import *

class teste(Database):
    def __init__(self):
        super().__init__()
        self.connect_to_database()

    def register_purchase(self):
        data_list = []  # LIsta vazia que vai pegar os valores
        arg = {'ID do produto:': int, 'Quantidade comprada:': int,
               'Valor da compra:': float,
               'Nome do cliente:': str}
        # Dicionário com o nome das perguntas e valores como tipos de dados

        for nome, tipo in arg.items():  # dois argumentos no loop, key e valor
            quest = tipo(input(f'Digite {nome} '))
            data_list.append(quest)  # A cada rodada do loop, acrescent

        try:
            self.cursor.execute('''
                UPDATE produtos
                set quantidade_produto = quantidade_produto - %s
                where id_product = %s
            ''', (data_list[1], data_list[0]))
            self.connection.commit()
            self.connection.close()

        except psycopg2.Error as erro_db:
            print(f'Erro {erro_db}')







testee = teste()

testee.register_purchase()