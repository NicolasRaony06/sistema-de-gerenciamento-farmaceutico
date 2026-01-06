#implementacao de classe Venda
from src.core.funcionario import Funcionario
from datetime import datetime
from decimal import Decimal
from src.utils.gerador_id import getIdProduto

class Venda:
    allIds = []
    def __init__(self, id: int, funcionario: Funcionario):
        self.__id = id
        self.__funcionario = funcionario
        self.__precoTotal = Decimal("0")
        self.__produtos = []
        self.__dataVenda = datetime.now()
        self.__logAlteracoes = []

    def getId(self):
        '''Retorna ID de venda'''
        return self.__id
    
    def getFuncionario(self):
        '''Retorna um objeto do tipo Funcionario'''
        return self.__funcionario
    
    def getPrecoTotal(self):
        '''Retorna preco total da Venda'''
        return self.__precoTotal
    
    def getProdutos(self):
        '''Retorna lista com tuplas de produtos e suas quantidades'''
        return self.__produtos
    
    def adicionarProduto(self, produto, quantidade : int):
        '''Adiciona produto em Venda, caso produto ja exista, a sua quantidade e somada. Recebe como parametro um objeto do tipo Produto e uma quantidade inteira.'''
        from src.farmacia.produto import Produto
        if not isinstance(produto, Produto):
            raise ValueError('Metodo deve receber um objeto do tipo Produto')
        
        if quantidade < 0:
            raise ValueError('Quantidade deve ser maior que 0')
        
        for index, vendaProduto in enumerate(self.__produtos):
            if produto.__repr__() in vendaProduto:
                self.__produtos[index] = (produto, vendaProduto[1] + quantidade)
                return True
                
        self.__produtos.append((produto.__repr__(), quantidade))

    def setPrecoTotal(self, funcionario: Funcionario, valor: Decimal):
        '''Setter para alterar preco total da venda. Recebe um objeto do tipo Funcionario e um valor do tipo Decimal. Adiciona a atual modificacao ao Log de Alteracoes'''
        if valor > 0:
            self.__precoTotal = valor
            log = f'Data:{datetime.now()};Funcionario:{funcionario};Valor:{valor}'
            self.__logAlteracoes.append(log)

        raise ValueError("O valor de preço total deve ser maior que 0")