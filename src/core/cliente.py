#implementacao de classe Cliente
from src.core.pessoa import Pessoa
from datetime import datetime
class Cliente(Pessoa):
    def __init__(self,nome:str,cpf:str,data_nascimento:datetime, id_cliente):
        super().__init__(nome,cpf,data_nascimento)
        self.__id_cliente = id_cliente

    def get_id_cliente (self):
        self.get_cpf = self.__id_cliente
        return self.__id_cliente