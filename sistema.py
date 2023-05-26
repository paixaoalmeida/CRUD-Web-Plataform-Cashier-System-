from Produto import Produto as produto
from Cliente import Client


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
            produto.AddProductInfoAndQuerry()
            break
        elif sis_menu == 2:
            produto.ShowAllProducts()
            break
        elif sis_menu == 3:
            produto.RemoveProduct()
            break
        elif sis_menu == 4:
            Client.cadastro_cliente()
            break
        elif sis_menu == 0:
            break


#Rodando a função Main do programa
if __name__ == '__main__':
    Main()