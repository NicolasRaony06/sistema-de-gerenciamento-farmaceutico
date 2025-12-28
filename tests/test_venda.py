# teste de implementacoes - python -m tests.test_venda
from datetime import datetime
from src.farmacia.farmacia import Farmacia
from src.farmacia.venda import Venda
from src.core.funcionario import Funcionario

func = Funcionario('teste', '055.678.501-08', datetime(2000, 8, 25), 1500.0, 3)
farm = Farmacia("Pague mais")

#teste de id automatico
print(farm.getListaVendas())
farm.criarVenda(func)
print(farm.getListaVendas()[0].getId())
farm.criarVenda(func)
print(farm.getListaVendas()[1].getId())
farm.criarVenda(func)
print(farm.getListaVendas()[2].getId())