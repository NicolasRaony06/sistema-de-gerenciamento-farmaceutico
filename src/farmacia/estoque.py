class Estoque:
    def __init__(self):
        self.__produtos = {} # estrutura: {obj_produto: qtd}

    def get_produtos(self):
        return self.__produtos
    
    def adicionar_produto(self, produto, quantidade: int):
        from src.farmacia.produto import Produto
        if not isinstance(produto, Produto): # isso aqui serve pra evitar problemas de importacao circular
            raise ValueError("Parametro produto deve ser uma instacia do tipo Produto")
        
        for produto_estoque in self.__produtos.keys():
            if (produto == produto_estoque) or (produto.getId() == produto_estoque.getId()):
                raise ValueError("Produto já existe em estoque") # aqui verifica ser a referencia ao objeto de produto já tá em estoque.
            
        if quantidade < 0:
            raise ValueError("Quantidade deve ser maior que 0") # essa validação pode ser tirada caso estoque possa ter um produto sem disponibilidade de compra.
            
        self.__produtos.update({produto: quantidade}) # adiciona uma nova chave e valor em dicionario de produtos

    def remover_produto(self, id_produto, quantidade): # não mudei nada aqui, mas deve precisar de reajuste
        produtos_estoque = self.__produtos
        if id_produto in produtos_estoque:
            if produtos_estoque[id_produto]["quantidade"] >= quantidade:
                produtos_estoque[id_produto]["quantidade"] -= quantidade
                return True
            else:
                print('Quantidade insuficiente')
        else:
            print('Produto não encontrado.')
        return False