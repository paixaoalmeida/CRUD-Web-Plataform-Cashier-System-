#The purpose of this file is to make some tests in the code when i need to.

from Database import *
from functions_system import *



database = Database()

database.connect_to_database(SystemFunctions.pegar_nomes())

database.show_all_tables()