from Produto import Produto as produto
from Cliente import *
from database.Database import *
from res.functions_system import *

sys_functions = SystemFunctions()
client = Cliente()
#------------------------------------------CÓDIGO--------------------------------

#Função Main - Parte principal
def Main():
    while True:
        sis_menu = int(input('''
            Sistema de caixa.
            
            1 - Adicionar Produto/Informação
            2 - Mostrar todos os produtos
            3 - Remover produto do estoque
            4 - Cadastrar um cliente
            0 - Sair
        '''))

        #Function of the cashier and function to ask if user wants to leave the system
        if sis_menu == 1:
            produto.add_product()
            sys_functions.ask_to_leave()
        elif sis_menu == 2:
            produto.show_products()
            sys_functions.ask_to_leave()
        elif sis_menu == 3:
            produto.remove_product()
            sys_functions.ask_to_leave()
        elif sis_menu == 4:
            client.add_client()
            sys_functions.ask_to_leave()
        elif sis_menu == 0:
            break


#Rodando a função Main do programa
if __name__ == '__main__':
    Main()