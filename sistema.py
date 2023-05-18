# -*- coding: utf-8 -*-
import sys

class Produto():
    def __init__(self, preco, tipo):
        self.preco = preco
        self.tipo = tipo

    def MostrarPreco(self):
        return 'O preço é ' + self.preco
    
    
    def MostrarTipo(self):
        return 'O tipo é ' + self.tipo
    
produto = Produto(sys.argv[1], sys.argv[2])

print(produto.MostrarPreco())
print(produto.MostrarTipo())