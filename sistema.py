# -*- coding: utf-8 -*-
import sys #Lib to get the arguments
import psycopg2 #Lib to connect to de PostgreeSQL database
#CONNECTING TO DATABASE
conn = psycopg2.connect(database="Sistema_caixa",
                        host="localhost",
                        user="postgres",
                        password="teste",
                        port="5432")
cursor = conn.cursor()
#--------------------------------------------#------------------------------------#------------------

class Produto():
    def __init__(self):
        pass
    
    def AddProductInfoAndQuerry(self):
        prod_list = [] #LIsta vazia que vai pegar os valores
        arg = {'nome do produto:': str, 'preço do produto:': float, 'a quantidade:': int} 
        #Dicionário com o nome das perguntas e valores como tipos de dados 
    
        for nome, tipo in arg.items(): #dois argumentos no loop, key e valor
            quest = tipo(input(f'Digite {nome} '))
            prod_list.append(quest) #A cada rodada do loop, acrescenta o resultado a lista
        
        try:
            cursor.execute(f"""
            INSERT INTO produtos (nome_produto,preco_produto,quantidade_produto)
            VALUES(%s,%s,%s); 
            """, (prod_list[0], prod_list[1], prod_list[2])) #Usando a função %s para definir uma váriavel - função do C
            conn.commit() #Comitar as mudanças no banco
        except:
            print('Há algo de errado com os dados ou o banco!')

produto = Produto() #Colocando a classe produto dentro de um objeto



#Função Main - Parte principal
def Main():
    produto.AddProductInfo()



#Rodando a função Main do programa
if __name__ == '__main__':
    Main()
