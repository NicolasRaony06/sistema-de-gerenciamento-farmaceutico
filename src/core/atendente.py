#implementacao de classe Atendente
from src.core.funcionario import Funcionario

class Atendente(Funcionario):
    def __init__(self, nome, cpf, data_nascimento, salario_base, id: int):
        super().__init__(nome, cpf, data_nascimento, salario_base, id)

    def get_bonus(Self):
        pass

    def __repr__(self):
        return f'Atendente("{self.nome}", {self.get_cpf()}, "{self.get_data_nascimento()}", {self.get_salario_base()}, {self.get_id()})'