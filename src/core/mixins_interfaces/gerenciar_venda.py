class GerenciarVendaMixin:
    def registrar_venda(self):
        '''Registra nova venda em farmacia. E adiciona Venda em lista de vendas do funcionario.'''
        return self.getFarmacia()._criarVenda(self)
    
    def adicionar_produto_venda(self, id, quantidade):
        '''Adiciona produto em venda, ultima realizada por funcionario, caso produto esteja disponivel no estoque.'''
        estoque = self.getFarmacia()._estoque
        return estoque.remover_produto(self,id,quantidade)

    def adicionar_cliente_venda(self, cliente):
        '''Adiciona cliente em ultima venda registrada pelo funcionario.'''
        self.getVendasRealizadas()[-1].adicionarCliente(cliente)

    def finalizar_venda(self,venda):
        '''Finaliza ultima venda realizada pelo funcionario.'''
        return venda.finalizarVenda()
        
