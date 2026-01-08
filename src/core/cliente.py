#implementacao de classe Cliente
from src.core.pessoa import Pessoa
from datetime import datetime
class Cliente(Pessoa):
    def __init__(self,nome:str,cpf:str, id_cliente:str = None,data_nascimento=None,):
        super().__init__(nome,cpf,data_nascimento)
        self.__id_cliente = id_cliente if id_cliente else cpf
        self.__compras = [] # precisei implementar para testar venda

    def get_id_cliente (self):
        return self.__id_cliente
    
    def getCompras(self):    # precisei implementar para testar venda
        '''Retorna lista de compras'''
        return self.__compras

    def _addCompra(self, compra): # precisei implementar para testar venda
        '''Método protegido usado por Venda automaticamente quando cliente é adicionado.'''
        self.__compras.append(compra)
    
    def __str__(self):
        return f'Nome: {self.nome} | Id: {self.get_id_cliente()}'
    
    def __repr__(self):
        return f'Cliente("{self.nome}, "{self.get_cpf()}", "{self.__id_cliente}", "{self.get_data_nascimento()}")'