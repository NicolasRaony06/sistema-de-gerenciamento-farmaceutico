#implementacao de classe Gerente
from src.core.funcionario import Funcionario
from src.farmacia.estoque import Estoque
from src.farmacia.farmacia import Farmacia
from src.farmacia.produto import Produto
class Gerente(Funcionario, Estoque, Farmacia):
    def __init__(self, nome, cpf, data_nascimento, salario_base, id):
        super().__init__(nome, cpf, data_nascimento, salario_base, id)
       
    def cadastrar_funcionario(self, funcionario):
            self.funcionarios.append(funcionario)
            print(f"Funcionário {funcionario} cadastrado.")

    def excluir_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f"Funcionário {funcionario} removido.")
        else:
            print("Funcionário não encontrado.")

    def alterar_preco_produto(self, produto):
        id_produto = str(input("Id do produto ?"))
        if id_produto in self.get_produtos:
            novo_preco = float(input("Digite o novo preço: "))
            produto.preco = novo_preco
            print(f"Preço do produto {produto.nome} alterado para {novo_preco}.")
        else:
            print("produto não encontrado")

    def cadastrar_produto(self):
        produto = Produto()
        self.__produtos.append(produto)
        print(f"Produto {produto.nome} cadastrado com sucesso.")