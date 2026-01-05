#implementacao de classe Gerente
from src.core.funcionario import Funcionario
from src.core.mixins_interfaces.funcionalidades_gerente import FuncionalidadesGerente
from src.utils.gerador_id import getIdProduto

class Gerente(Funcionario,FuncionalidadesGerente):
    allIds = []
    def __init__(self,nome,cpf,data_nascimento,salario_base):
        super().__init__(nome,cpf,data_nascimento,salario_base, getIdProduto(self))

    def cadrastar_funcionario(self):
        pass
    def excluir_funcionario(self):
        pass
    def alterar_preco_produto(self):
        pass