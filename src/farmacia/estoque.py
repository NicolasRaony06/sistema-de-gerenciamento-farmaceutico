from src.utils.validacoes import validar_produto

class Estoque:
    def __init__(self):
        self.__produtos = {}

    def get_produtos(self):
        return self.__produtos

    def adicionar_produto(self, produto, quantidade: int):
        validar_produto(produto)
        p_id = produto.getId()
        if p_id in self.__produtos:
            self.__produtos[p_id]["quantidade"] += quantidade
        else:
            self.__produtos[p_id] = {
                "produto": produto,
                "quantidade": quantidade
            }

    def remover_produto(self, id, quantidade = None):
        '''Recebe um inteiro do Id de Produto e, remove ou reduz sua quantidade do estoque, caso parametro 'quantidade' tenha um valor inteiro positivo.'''
        produtos_estoque = self.__produtos
        for id_produto in produtos_estoque.keys():
            if id_produto == id:
                if quantidade > 0:
                    if self.produto_disponibilidade(produtos_estoque[id]["produto"], quantidade): #dupla verificacao, reutilizando metodo, pra caso seja um valor positivo, porem acima de permitido.
                        produtos_estoque[id]["quantidade"] -= quantidade
                        return True
                    raise ValueError("Produto em quantidade indisponível.")
                
                del produtos_estoque[id]
                return True    
     
    def consultar_produto_por_id(self, id_produto):
        if id_produto in self.__produtos:
            id = self.__produtos[id_produto]["produto"]
            quantidade = self.__produtos[id_produto]["quantidade"]
            return id.nome,quantidade #Tupla: (Nome,Quantidade)
        else:
            return False

    def consultar_produto_por_nome(self, nome):
        for registro in self.__produtos.values():
            produto = registro["produto"]
            quantidade = registro["quantidade"]

            if produto.nome == nome:
                return produto.nome,quantidade #Tupla: (Nome,Quantidade)
        
        return False

    def produto_disponibilidade(self, produto, quantidade):
        '''Checa se produto em quantidade passada está disponível para ser vendido. Retorna valor booleano.'''
        validar_produto(produto)
        produto_estoque = self.__produtos.get(produto.getId())
        if produto_estoque:
            if produto_estoque.get("quantidade") >= quantidade:
                return True
        return False


    
