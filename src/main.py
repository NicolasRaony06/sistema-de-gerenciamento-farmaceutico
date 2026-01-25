# ---------------- IMPORTS ----------------
import os
import time
from datetime import datetime
from decimal import Decimal

from src.core.atendente import Atendente
from src.core.cliente import Cliente
from src.core.funcionario import Funcionario
from src.core.gerente import Gerente
from src.core.pessoa import Pessoa
from src.core.mixins_interfaces import *

from src.farmacia.farmacia import Farmacia
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto
from src.farmacia.venda import Venda


# ---------------- INSTÂNCIAS PRINCIPAIS ----------------
farmacia = Farmacia('Farmacia Holanda')
estoque = farmacia._estoque
gerente = farmacia._registrarGerente(
    'Carlos',
    '13032112390',
    '1-1-8909',
    1200,
    123
)


# ---------------- FUNÇÕES AUXILIARES ----------------
def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------------- PRODUTOS ----------------
def cadrastar_produto():
    print("\n--- CADASTRAR NOVO PRODUTO ---")
    nome = input("Nome: ")
    preco = input("Preço: ")
    fabricante = input("Fabricante: ")
    qntd = int(input("Quantidade: "))

    produto = Produto(nome, preco, fabricante)
    gerente.adicionar_produto_estoque(produto, qntd)

    input("\nPressione Enter para voltar ao menu...")


def remover_produto():
    print("\n--- REMOVER PRODUTO ---")
    id_produto = int(input("Digite o Id do Produto: "))
    gerente.remover_produto(id_produto)

    input("\nPressione Enter para voltar ao menu...")


def alterar_preco_produto():
    print("\n--- ALTERAR PREÇO ---")
    id_produto = int(input("Digite o ID do produto: "))
    novo_preco = Decimal(input("Digite o novo preço: "))

    produto , _ = gerente.consultar_produto_por_id(id_produto)
    gerente.alterar_preco_produto(produto, novo_preco)

    input("\nPressione Enter para voltar ao menu...")


def listar_produtos():
    print("\n--- ESTOQUE ATUAL ---")
    if not gerente.consultar_estoque():
        print("Estoque vazio!")
    else:
        print(gerente.consultar_estoque())

    input("\nPressione Enter para voltar ao menu...")


def buscar_produto_id():
    print("\n--- BUSCAR PRODUTO POR ID ---")
    id_produto = int(input("Digite o Id do Produto: "))

    resultado = gerente.consultar_produto_por_id(id_produto)
    if resultado is None:
        print("Produto não encontrado")
    else:
        print(resultado)

    input("\nPressione Enter para voltar ao menu...")


def buscar_produto_nome():
    print("\n--- BUSCAR PRODUTO POR NOME ---")
    nome = input("Digite o Nome do Produto: ")

    resultado = gerente.consultar_produto_por_nome(nome)
    if resultado is None:
        print("Produto não encontrado")
    else:
        print(resultado)

    input("\nPressione Enter para voltar ao menu...")


# ---------------- FUNCIONÁRIOS ----------------
def cadrastar_funcionario():
    print("\n--- CADASTRAR FUNCIONÁRIO ---")
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")

    data_str = input("Data de nascimento (dd-mm-aaaa): ")
    data_nascimento = datetime.strptime(data_str, "%d-%m-%Y").date()

    salario = Decimal(input("Salário do funcionário: "))
    cargo = str(input("Digite o cargo do funcionário: (atendente/repositor): "))
    gerente.cadrastar_funcionario(cargo,nome, cpf, data_nascimento, salario)

    print("Funcionário cadastrado!")
    input("\nPressione Enter para voltar ao menu...")


def excluir_funcionario():
    print("\n--- EXCLUIR FUNCIONÁRIO ---")
    id_funcionario = int(input("Digite o Id do funcionário: "))

    funcionario = gerente.getFarmacia().getFuncionarioPorId(id_funcionario)
    gerente.excluir_funcionario(funcionario)

    input("\nPressione Enter para voltar ao menu...")


def listar_funcionarios():
    print("\n--- LISTA DE FUNCIONÁRIOS ---")
    print(gerente.consultar_lista_funcionario())

    input("\nPressione Enter para voltar ao menu...")


# ---------------- VENDAS ----------------
def vender_produto():
    venda = gerente.registrar_venda()

    while True:
        id_produto = int(input("ID do produto (0 para finalizar): "))

        if id_produto == 0:
            break

        quantidade = int(input("Quantidade: "))

        try:
            # busca no estoque
            produto, qtd_estoque = gerente.consultar_produto_por_id(id_produto)

            if quantidade > qtd_estoque:
                print("Quantidade insuficiente em estoque")
                continue

            # adiciona na venda
            gerente.adicionar_produto_venda(produto,quantidade)


            print("Produto adicionado à venda!")

        except ValueError as e:
            print(f"Erro: {e}")

    gerente.finalizar_venda()
    print("ITENS DA VENDA:")
    for item in venda.getProdutos():
        print(item)
    print("PREÇO TOTAL")
    print(venda.getPrecoTotal())
    
    input("\nPressione Enter para voltar ao menu...")


# ---------------- MENU ----------------
def menu():
    limpar_tela()
    print("=" * 30)
    print(" SISTEMA DE FARMÁCIA v1.0 ")
    print(" ÁREA DO GERENTE ")
    print("=" * 30)
    print("[1]  - Cadastrar Produto")
    print("[2]  - Remover Produto")
    print("[3]  - Alterar Preço de Produto")
    print("[4]  - Consultar Estoque")
    print("[5]  - Buscar Produto por Id")
    print("[6]  - Buscar Produto por Nome")
    print("[7]  - Cadastrar Funcionário")
    print("[8]  - Excluir Funcionário")
    print("[9]  - Listar Funcionários")
    print("[10] - Vender Produto")
    print("[0]  - Sair")
    print("=" * 30)


# ---------------- MAIN ----------------
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadrastar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            alterar_preco_produto()
        elif opcao == '4':
            listar_produtos()
        elif opcao == '5':
            buscar_produto_id()
        elif opcao == '6':
            buscar_produto_nome()
        elif opcao == '7':
            cadrastar_funcionario()
        elif opcao == '8':
            excluir_funcionario()
        elif opcao == '9':
            listar_funcionarios()
        elif opcao == '10':
            vender_produto()
        elif opcao == '0':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida!")
            time.sleep(1)


# ---------------- PONTO DE ENTRADA ----------------
if __name__ == "__main__":
    main()
