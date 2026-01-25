#implementacao de classe Venda
from datetime import datetime
from decimal import Decimal, ROUND_DOWN
from src.utils.gerador_id import getIdProduto
from src.utils.validacoes import validar_cliente, validar_produto

class Venda:
    allIds = []
    def __init__(self, id : int, funcionario):
        self.__id = id
        self.__funcionario = funcionario
        self.__cliente = None
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
        '''Retorna preço total da Venda'''
        return self.__precoTotal
    
    def getProdutos(self):
        '''Retorna lista com tuplas de produtos e suas quantidades'''
        return self.__produtos
    
    def getLogAlteracoes(self):
        '''Retorna lista de tuplas sobre alterações de Venda'''
        return self.__logAlteracoes
    
    def getCliente(self):
        '''Retorna cliente caso exista em Venda'''
        return self.__cliente
    
    def adicionarCliente(self, cliente):
        '''Adiciona um cliente em Venda. Recebe objeto de cliente.'''
        validar_cliente(cliente)

        if self.__precoTotal :
            raise PermissionError('Venda já finalizada. Não é mais possível adicionar cliente')
        
        self.__cliente = cliente
        

        log =(
            f'adicionarCliente()', 
            f'Data:{datetime.now()}',
            f'{cliente.__repr__()}'
        )

        self.__logAlteracoes.append(log)
    
    def adicionarProduto(self, produto, quantidade: int):
        if self.__precoTotal:
            raise PermissionError("Venda já finalizada")

        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        item = {
            "id": produto.getId(),
            "nome": produto.getNome(),
            "preco_unitario": produto.getPreco(),  # ← preço congelado
            "quantidade": quantidade
        }

    # verifica se produto já existe na venda
        for registro in self.__produtos:
            if registro["id"] == item["id"]:
                registro["quantidade"] += quantidade
                return

        self.__produtos.append(item)

    def finalizarVenda(self):
        if self.__precoTotal :
            raise PermissionError("Venda já finalizada")

        total = Decimal("0")
        for produto, quantidade in self.__produtos:
            total += produto.getPreco() * quantidade

        self.__precoTotal = total
        self.__logAlteracoes.append(("venda_finalizada", datetime.now(), total))
        
    def __subTotal(self):
        '''Método privado para calcular subtotal da venda.'''
        from src.farmacia.produto import Produto
        subTotal = Decimal(0)
        for itemVenda in self.__produtos:
            try:
                produto = eval(itemVenda[0])
            except Exception as erro:
                raise TypeError(f"Erro ao instanciar Produto: {erro}")

            subTotal += produto.getPreco() * itemVenda[1]

        return subTotal
        
    def __repr__(self):
        return f'Venda({self.__id}, {self.__funcionario.__repr__()})'