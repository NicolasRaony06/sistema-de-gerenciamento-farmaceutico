# teste de implementacoes - python -m tests.test_venda
from datetime import datetime
from src.farmacia.farmacia import Farmacia
from src.core.atendente import Atendente
from src.core.cliente import Cliente
from src.farmacia.produto import Produto
from decimal import Decimal

atendente = Atendente('teste', '055.678.501-08', datetime(2000, 8, 25), 1500.0, 3)
farm = Farmacia("Pague mais")

#teste de id automatico
print(farm.getListaVendas())
farm.criarVenda(atendente)
# print(farm.getListaVendas()[0].getId())
# farm.criarVenda(atendente)
# print(farm.getListaVendas()[1].getId())
# farm.criarVenda(atendente)
# print(farm.getListaVendas()[2].getId())

produto_teste = Produto('Amitril',2.90,'Cimed')
produto_teste2 = Produto('Cesol',8.25,'Farmacol')

farm.getListaVendas()[0].adicionarProduto(produto_teste, 1)

print(farm.getListaVendas()[0].getProdutos())

farm.getListaVendas()[0].adicionarProduto(produto_teste, 1)
print(farm.getListaVendas()[0].getProdutos())

farm.getListaVendas()[0].adicionarProduto(produto_teste2, 2)
print(farm.getListaVendas()[0].getProdutos())

farm.getListaVendas()[0].adicionarCliente(atendente,Cliente('teste', '123.458.136-08', 12))
print(farm.getListaVendas()[0].getCliente())
print(farm.getListaVendas()[0].getLogAlteracoes())

print(farm.getListaVendas()[0].getPrecoTotal()) 
farm.getListaVendas()[0].setPrecoTotal(atendente) # finalizando venda
print(farm.getListaVendas()[0].getPrecoTotal()) 

# farm.getListaVendas()[0].adicionarProduto(produto_teste2, 2) # testando erro de tentar adicionar produto com venda finalizada

# farm.getListaVendas()[0].adicionarCliente(atendente,Cliente('teste', '123.458.136-08', 12)) # testando add cliente apos venda finalizada

print(farm.getListaVendas()[0].getLogAlteracoes()) # testando logs
