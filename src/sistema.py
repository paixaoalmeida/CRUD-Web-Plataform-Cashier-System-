from src.cliente import *
from src.produto import *


#Storing the classes into objects
product = Produto()
product_register = RegisterProduct()
client = Cliente()


def ask_to_leave():
    """
    This function asks every time the user does something either he
    wants to stay in the loop or not

    It does know the difference between upper and lower case letters

    -If the user inputs 'S', it does exit the program with 0 code
    -if the user inputs 'N', it does break the loop, and continues in the
    loop of the main() function
    """
    while True:
        quest = str(input('Deseja sair? S/N')).upper()
        try:
            if quest == 'S':
                exit(0)
            elif quest == 'N':
                break
        except ValueError:
            print('Digite S ou N!')


def main():
    while True:
        sis_menu = int(input('''
            Sistema de caixa.
            
            1 - Adicionar Produto/Informação
            2 - Mostrar todos os produtos
            3 - Remover produto do estoque
            4 - Cadastrar um cliente
            5 - Registrar uma compra
            0 - Sair
        '''))

        '''
        This if-statement block was made like this cuz the psycopg2
        library (used to query the database) only runs in python3.8 <
        
        It does use the functions of the modules 'cliente' and 'produtos'
        (which are listed/imported at the beginning of this file)
        
        What does it have?
        -Function to remove product
        -Function to show all products
        -Function to add products
        -Function to add cliente
        -Function to register a purchase
        '''
        if sis_menu == 1:
            product.add_product()
            ask_to_leave()
        elif sis_menu == 2:
            product.show_products()
            ask_to_leave()
        elif sis_menu == 3:
            product.remove_product()
            ask_to_leave()
        elif sis_menu == 4:
            client.add_client()
            ask_to_leave()
        elif sis_menu == 5:
            RegisterProduct.register_purchase()
        elif sis_menu == 0:
            break


#Rodando a função Main do programa
if __name__ == '__main__':
    main()
