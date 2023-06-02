from Produto import Produto as produto
from Cliente import *

#------------------------------------------CÓDIGO--------------------------------

#Fuction who asks if the user wants to leave or not
def ask_to_leave(self=None):
    while True:
        quest = str(input('Deseja sair? S/N')).upper()
        try:
            if quest == 'S':
                exit(0)
            elif quest == 'N':
                break
        except ValueError:
            print('Digite S ou N!')

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
            ask_to_leave()
        elif sis_menu == 2:
            produto.show_products()
            ask_to_leave()
        elif sis_menu == 3:
            produto.remove_product()
            ask_to_leave()
        elif sis_menu == 4:
            Cliente.add_client()
            ask_to_leave()
        elif sis_menu == 0:
            break


#Rodando a função Main do programa
if __name__ == '__main__':
    Main()