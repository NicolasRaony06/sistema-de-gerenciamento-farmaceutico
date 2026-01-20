class GerenciarEstoqueMixin:
    def adicionar_produto_estoque(self,produto , quantidade):
        """Adiciona qtd ao estoque chamando o metodo do obj Estoque"""
        estoque = self.getFarmacia()
        estoque._estoque.adicionar_produto(produto, quantidade)
        
    def remover_produto(self, id, quantidade = None):
       estoque = self.getFarmacia()
       estoque.remover_produto(id,quantidade)
            
    def consultar_estoque(self):
        estoque = self.getFarmacia()._estoque
        if not estoque.get_produtos():
            return False

        return {
        
            dados["produto"].nome: dados["quantidade"]
            for dados in estoque.get_produtos().values()
        }
    
    def consultar_produto_por_id(self, id_produto):
        estoque = self.getFarmacia()._estoque
        return estoque.consultar_produto_por_id(id_produto)

    def consultar_produto_por_nome(self, nome ):
        estoque = self.getFarmacia()._estoque
        return estoque.consultar_produto_por_nome(nome)