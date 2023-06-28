from src.produto import *

teste = Database()

teste.connect_to_database()

print(teste.show_all_products())

