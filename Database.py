import psycopg2
import functions_system as funcimp

class Database:
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
        try:
            self.cursor.execute('''
                SELECT * FROM produtos
            ''')
            all_itens = self.cursor.fetchall()
            # Como é uma tupla dentro de uma lista, eu preciso fornecer dois indexes

            # Dando um loop em todos os valores das tuplas retornadas
            for item in all_itens:
                print(f'''
                        nome: {item[0]}
                        preço: R${item[1]}
                        quantidade: {item[2]}
                    ''')
        except psycopg2.Error as error_db:
            print('Algo deu errado! Siga o erro do banco abaixo: \n')
            print(f'{error_db}\n')
            print(error_db.diag)

    
    
    def remove_products(self):
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
        prod_list = []  # LIsta vazia que vai pegar os valores
        arg = {'nome do produto:': str, 'preço do produto:': float, 'a quantidade:': int}
        # Dicionário com o nome das perguntas e valores como tipos de dados

        for nome, tipo in arg.items():  # dois argumentos no loop, key e valor
            quest = tipo(input(f'Digite {nome} '))
            prod_list.append(quest)  # A cada rodada do loop, acrescenta o resultado a lista

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
        

