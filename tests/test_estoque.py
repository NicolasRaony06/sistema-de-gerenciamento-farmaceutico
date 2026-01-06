# teste de implementacoes
# python -m tests.test_estoque
from src.utils.gerador_id import getIdProduto
from src.core.gerente import Gerente
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto
estoque = Estoque() 
g = Gerente('João', '12345678900', '1990-01-01','1200',1)
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
g.adicionar_produto_estoque(p1,12,estoque)
g.adicionar_produto_estoque(p2,24,estoque)
print(f'Estoque Antes da venda: {g.consultar(estoque)}')
g.vender_produto(p1.getId(),2,estoque)
g.vender_produto(p2.getId(),4,estoque)
print(estoque.consultar_quantidade_por_id(p1.getId()))
print(f'Estoque Depois da venda: {g.consultar(estoque)}')