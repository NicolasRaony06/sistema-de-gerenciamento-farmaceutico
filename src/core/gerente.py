#implementacao de classe Gerente
from src.core.funcionario import Funcionario
from src.core.mixins_interfaces.funcionalidades_gerente import FuncionalidadesGerente

class Gerente(Funcionario,FuncionalidadesGerente):
    def __init__(self,nome,cpf,data_nascimento,salario_base, id: int):
        super().__init__(nome,cpf,data_nascimento,salario_base, id)

    def get_bonus(Self):
        pass

    def cadrastar_funcionario(self):
        pass
    def excluir_funcionario(self):
        pass
    def alterar_preco_produto(self):
        pass

    def __repr__(self):
        return f'Gerente("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'
