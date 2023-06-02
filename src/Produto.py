from src.database.Database import Database

#Putting the class into an object
database = Database()
# --------------------------------------------#------------------------------------#-----------------

class Produto():
    def __init__(self):
        pass

    
    def add_product():
        database.connect_to_database()
        database.add_product_and_query()

    
    def show_products():
        database.connect_to_database()
        database.show_all_products()


    def remove_product():
        database.connect_to_database()
        database.remove_products()


    #def register_purchase():