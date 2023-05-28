#EM PRODUÇÃO, LIB PSYCOPG2 SÓ FUNCIONA ABAIXO DO PYTHON 9
import psycopg2
import functions_system as funcimp
from Database import *

class Client:
    def __init__(self):
        pass

    def cadastro_cliente(cls):

        try:
            with psycopg2.connect(database="postgrees",host="localhost",user="postgres",password="teste",port="5432") as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO clientes(nome_cliente,cpf_cliente)
                    VALUES(%s,%s);
                    ''',(
                        funcimp.SystemFunctions.pegar_nomes())) 
                #Passando a função pegar nomes no valor do INSERT
                conn.commit() and conn.close 
                #Atualizando e fechando a conexão com o banco

        except psycopg2.Error as erro:
            print(f'{erro}')
            exit(1)




