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
        
        match (sis_menu):
            case 1:
                produto.AddProductInfoAndQuerry()
            case 2:
                produto.ShowAllProducts()
            case 3:
                produto.RemoveProduct()
            case 4:
                Client.cadastro_cliente()
            case _:
                ('Digite uma das opções válidas!')


#Rodando a função Main do programa
if __name__ == '__main__':
    Main()