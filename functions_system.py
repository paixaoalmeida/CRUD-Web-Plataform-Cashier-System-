class SystemFunctions:
    def __init__(self):
        pass

    @classmethod
    def pegar_nomes(cls):
        prod_list = []  # LIsta vazia que vai pegar os valores
        arg = {'nome do cliente:': str, 'CPF do cliente:': str}
        # Dicionário com o nome das perguntas e valores como tipos de dados

        for nome, tipo in arg.items():  # dois argumentos no loop, key e valor
            quest = tipo(input(f'Digite {nome} '))
            prod_list.append(quest)  # A cada rodada do loop, acrescenta o resultado a lista
        return prod_list[0],prod_list[1]