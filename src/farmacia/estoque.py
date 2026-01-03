class Estoque:
    def __init__(self):
        self.__produtos = {} 

    def get_produtos(self):
        return self.__produtos
    
    def adicionar_produto(self, produto, quantidade):
        produtos_estoque = self.__produtos
        if produto.getId() in produtos_estoque:
            produtos_estoque[produto.getId()]["quantidade"] += quantidade
        else:
            produtos_estoque[produto.getId()] = {
                "produto": produto,
                "quantidade": quantidade
            }
    def remover_produto(self, id_produto, quantidade):
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