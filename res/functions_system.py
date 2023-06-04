"""
Library to make some random tests in the code
and all kinda bullshit i need
"""


class SystemFunctions:
    """
    This function was made to take the user's input

    It does add some key-values to a dictionary and iterates
    over a for loop between the key and value

    This way we can make all the questions we want just in one loop,
    and ensure error handling (user cant type anything he wants and get away with it)

    Finally, we do retun the indexes 0 and 1 of the user inputs, this indexes are
    being used in the 'cliente.py' module in the add_client method
    """
    def __init__(self):
        pass

    def pegar_nomes():
        prod_list = []  # LIsta vazia que vai pegar os valores
        arg = {'nome do cliente:': str, 'CPF do cliente:': str}

        for nome, tipo in arg.items():
            quest = tipo(input(f'Digite {nome} '))
            prod_list.append(quest)

        return prod_list[0], prod_list[1]

