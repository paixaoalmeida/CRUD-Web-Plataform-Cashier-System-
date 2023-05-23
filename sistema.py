from Produto import Produto as produto

#------------------------------------------CÓDIGO--------------------------------

#Função Main - Parte principal
def Main():
    while True:
        sis_menu = int(input('''
            Sistema de caixa.
            
            1 - Adicionar Produto/Informação
            0 - Sair
        '''))
        if sis_menu == 1:
            produto.AddProductInfoAndQuerry()
            break
        elif sis_menu == 0:
            exit(0)

#Rodando a função Main do programa
if __name__ == '__main__':
    Main()