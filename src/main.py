import os
import time
#python -m src.main 
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
farmacia = Farmacia('Farmacia Holanda')
estoque = farmacia._estoque
gerente = farmacia._registrarGerente('Carlos','13032112390','1-1-8909',1200,123)
def limpar_tela():
    """Função auxiliar para limpar o console e deixar o menu bonito."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cadrastar_produto():
    print("\n--- CADASTRAR NOVO MEDICAMENTO ---") 
    nome = input("Nome: ") 
    preco = input("Preço: ") 
    fabricante = input("Fabricante: ") 
    qntd = input("Quantidade: ") 
    p1 = Produto(nome,preco,fabricante) 
    gerente.adicionar_produto_estoque(p1,qntd) 
    input("\nPressione Enter para voltar ao menu...") 

def alterar_preco_produto():
        print("\n--- ALTERAR PREÇO ---") 
        id_produto = int(input("Digite o ID do produto: "))
        novo_preco = Decimal(input("Digite o novo preço: "))

        produto, _ = gerente.consultar_produto_por_id(id_produto)

        gerente.alterar_preco_produto(produto, novo_preco)
        input("\nPressione Enter para voltar ao menu...") 

def remover_produto():
    print("\n--- REMOVER PRODUTO ---") 
    id = int(input("Digite o Id do Produto: "))
    gerente.remover_produto(id)
    input("\nPressione Enter para voltar ao menu...") 

def listar_medicamentos():
    print("\n--- ESTOQUE ATUAL ---")
    print("          NOME | PREÇO | FABRICANTE | ID")
    print(gerente.consultar_estoque())
    input("\nPressione Enter para voltar ao menu...")

def buscar_medicamento_id():
    print("\n--- BUSCAR MEDICAMENTO ---")
    id = int(input("Digite o Id do Produto: "))
    if gerente.consultar_produto_por_id(id) is None:
        print("Produto não encontrado")
    else:
        print(gerente.consultar_produto_por_id(id))

    input("\nPressione Enter para voltar ao menu...")

def buscar_medicamento_nome():
    print("\n--- REALIZAR VENDA ---")
    nome = str(input("Digite o Nome do Produto: "))
    if gerente.consultar_produto_por_nome(nome) is None:
        print("Produto não encontrado")
    else:
        print(gerente.consultar_produto_por_nome(nome))
    input("\nPressione Enter para voltar ao menu...")

def menu():
    """Exibe as opções para o usuário."""
    limpar_tela()
    print("="*30)
    print(" SISTEMA DE FARMÁCIA v1.0 ")
    print("="*30)
    print("[1] - Cadastrar Produto")
    print("[2] - Remover Produto")
    print("[3] - Alterar Preço de Produto")
    print("[4] - Consultar Estoque")
    print("[5] - Buscar Produto por Id")
    print("[6] - Buscar Produto por Nome")
    print("[7] - Excluir Funcionário")
    print("[8] - Cadrastar Funcionário")
    print("[0] - Sair")
    print("="*30)

def main():
    """Função Principal (Gerente do Programa)"""
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
            listar_medicamentos()
        elif opcao == '0':
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida!")
            time.sleep(1) # Espera 1 segundo para o usuário ler o erro

# --- PONTO DE ENTRADA ---
# Isso garante que a main só rode se executarmos este arquivo diretamente
if __name__ == "__main__":
    main()