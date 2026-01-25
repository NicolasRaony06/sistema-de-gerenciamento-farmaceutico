# teste de implementacoes
# python -m tests.test_estoque
from src.farmacia.farmacia import Farmacia
from src.core.gerente import Gerente
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto
farmacia = Farmacia("SLA")
estoque = Estoque() 
g = Gerente('João', '12345678900', '1990-01-01','1200',1,farmacia,123)
p1 = Produto('Dipirona-25mg-Comprimido',2.30,'Cimed')
p2 = Produto('Dorflex-5mg-Comprimido',1.90,'Sanofi')
print(50*'-')
print('INFORMAÇÕES GERAIS DO FUNCIONARIO')
print(f'NOME: {g.nome}')
print(f'CPF: {g.get_cpf()}')
print(f'NASCIMENTO: {g.get_data_nascimento()}')
print(f'SALÁRIO: {g.get_salario_base()}')
print(f'ID: {g.get_id()}')
print(50*'-')
print('TESTANDO METODOS DE FUNCIONARIO')
g.adicionar_produto_estoque(p1,12)
g.adicionar_produto_estoque(p2,24)
#print(estoque.produto_disponibilidade(p2.nome,12))
print(g.consultar_estoque())
g.remover_produto(p1.getId(),2)
print(g.consultar_estoque())
print(g.consultar_produto_por_id(p1.getId()))