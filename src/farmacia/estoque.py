class Estoque:
    def __init__(self):
        self.__produtos = {} 

    def get_produtos(self):
        return self.__produtos

    def adicionar_produto(self, produto, quantidade: int):
        p_id = produto.getId()
        if p_id in self.__produtos:
            self.__produtos[p_id]["quantidade"] += quantidade
        else:
            self.__produtos[p_id] = {
                "produto": produto,
                "quantidade": quantidade
            }
            
    def consultar_quantidade_por_id(self, id_produto):
        if id_produto in self.__produtos:
            nome = self.__produtos[id_produto]["produto"]
            quantidade = self.__produtos[id_produto]["quantidade"]
        return f"ID: {id_produto} | Nome: {nome.nome} | Quantidade: {quantidade}"
    
    def consultar_quantidade_por_nome(self, nome):
        for nome in self.__produtos.values():
            produto = nome["produto"]
            quantidade = nome["quantidade"]
            return f"Quantidade de {produto.nome}: {quantidade:.2f}"
        return 0
    
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