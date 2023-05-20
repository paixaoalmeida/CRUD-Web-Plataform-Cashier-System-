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
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade



#Código em construção!!


def Main():
    list = []
    arg = ['nome do produto', 'preço do produto','a quantidade']

    for name in arg:
        quest = input(f"Digite {name} ")
        list.append(quest)
    print(list)


if __name__ == '__main__':
    Main()
