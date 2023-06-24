from src.produto import *

teste = Database()

teste.connect_to_database()

print(type(teste.show_all_products()))