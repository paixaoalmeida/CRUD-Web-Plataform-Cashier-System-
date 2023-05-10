#Projeto de um gerenciamento de estoque com integraçõesc
class Product():
    def __init__(self,nome, categoria, fornecedor, preco_compra,preco_venda,quantidade_estoque):
        self.nome = nome
        self.categoria = categoria
        self.fornecedor = fornecedor
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade_estoque = quantidade_estoque
    