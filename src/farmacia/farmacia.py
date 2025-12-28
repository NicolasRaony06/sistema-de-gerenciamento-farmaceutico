#implementacao de classe Farmacia
from decimal import Decimal
from src.core.funcionario import Funcionario
from src.core.atendente import Atendente
from src.core.gerente import Gerente
from src.farmacia.venda import Venda
from random import randint

class Farmacia:
    def __init__(self, nome : str):
        self.nome = nome
        self.__listaVendas = []
        self.gerente = None
        self.funcionarios = []

    def __getFreeId(self):
        '''Metodo privado que verifica todos os ids existentes de venda e retorna um novo int unico aleatorio.'''
        allIds = []
        for venda in self.__listaVendas:
            allIds.append(venda.getId())

        Id = 0
        while Id in allIds:
            Id = randint(1, 2048)
        return Id

    def getListaVendas(self):
        '''Retorna uma lista contendo todos os objetos de Venda registrados'''
        return self.__listaVendas
    
    def criarVenda(self, funcionario: Funcionario):
        '''Cria e retorna um objeto do tipo Venda. Adiciona obejto em Lista de Vendas e retorna seu indice'''
        venda = Venda(self.__getFreeId(), funcionario)
        self.__listaVendas.append(venda)

        return self.__listaVendas.index(venda)
        
    def registrarGerente(self):
        '''Recebe como parametros atributos de um Gerente e cria um novo objeto do tipo Gerente.'''
        self.gerente = Gerente() # a ser implementado apos a criacao de gerente
        pass

    def registrarAtendente(self):
        '''Recebe como parametros atributos de um Atendente e cria um novo objeto do tipo Atendente. Retorna seu indice na lista de funcionarios.'''
        atendente = Atendente()
        self.funcionarios.append(atendente)
        return self.funcionarios.index(atendente)


