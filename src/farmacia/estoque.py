
from .produto import Produto
from core.funcionario import Funcionario

class Estoque:
    def __init__(self):
        self.produtos = {}  # chave = id do produto

    def adicionar_produto(self, produto, quantidade):
        if produto.id in self.produtos:
            self.produtos[produto.id]["quantidade"] += quantidade
        else:
            self.produtos[produto.id] = {
                "produto": produto,
                "quantidade": quantidade
            }

    def vender_produto(self, id_produto, quantidade):
        if id_produto in self.produtos:
            if self.produtos[id_produto]["quantidade"] >= quantidade:
                self.produtos[id_produto]["quantidade"] -= quantidade
                return True
        return False

    def consultar(self):
        if not self.produtos:
            return "Estoque vazio"

        return {
            dados["produto"].nome: dados["quantidade"]
            for dados in self.produtos.values()
        }