from Produto import Produto as produto
from Cliente import Cliente
from Database import * 

cliente = Cliente()

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
        
        if sis_menu == 1:
            produto.add_product()
            break
        elif sis_menu == 2:
            produto.show_products()
            break
        elif sis_menu == 3:
            produto.remove_product()
            break
        elif sis_menu == 4:
            cliente.add_client()
            break
        elif sis_menu == 0:
            break


#Rodando a função Main do programa
if __name__ == '__main__':
    Main()