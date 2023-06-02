#EM PRODUÇÃO, LIB PSYCOPG2 SÓ FUNCIONA ABAIXO DO PYTHON 9
from res.functions_system import SystemFunctions as functions_system
from database.Database import *

#Creating a child class, this way i will have all the atributes from the database class and use it here
class Cliente(Database): 
    def __init__(self):
        super().__init__() #Chamado os métodos da classe pai
        self.connect_to_database()

    def add_client(self=None):
        try:
            self.cursor.execute('''
                INSERT INTO clientes(nome_cliente,cpf_cliente)
                VALUES(%s,%s);
                ''',(
                    functions_system.pegar_nomes())) 
                    #Passando a função pegar nomes no valor do INSERT
            self.connection.commit()
            self.connection.close()
                #Atualizando e fechando a conexão com o banco
    
        except psycopg2.Error as erro:
            print(f'{erro}')
            exit(1)



