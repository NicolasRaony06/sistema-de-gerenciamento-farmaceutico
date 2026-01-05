from src.utils.gerador_id import getIdProduto

class Produto:
    allIds = []
    def __init__(self, nome, preco, fabricante):
        self.__id = getIdProduto(self)
        self.nome = nome
        self.__preco = preco
        self.fabricante = fabricante
        self.__logAlteracoes = []

    def getId(self):
        return self.__id
    
    def getPreco(self):
        return self.__preco
    
    def __repr__(self):
        return f'Produto({self.nome}, {self.__preco}, {self.fabricante})'