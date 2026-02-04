from src.utils.tela import limpar_tela , VERDE , AZUL , AMARELO ,VERMELHO ,RESET , NEGRITO
import time
from datetime import datetime
from decimal import Decimal , InvalidOperation
from src.utils.validacoes import *
from src.core.mixins_interfaces import *
from src.farmacia.produto import Produto
#from src.main import login


def iniciar_login_atendente(atendente,farmacia):

# ---------------- VENDAS ----------------
    def vender_produto():
        limpar_tela()
        venda = atendente.registrar_venda()
        opc_cliente = input("Deseja Adicionar Cliente a Venda?(S/N) ")
        if opc_cliente == 'S':
            cpf = str(input("Digite o Cpf do cliente: "))
            if not farmacia.getClientePorCpf(cpf):
                print("Cliente não cadrastado no sistema!")
                nome = str(input("Nome do cliente: "))
                data_str = input("Data de nascimento (dd-mm-aaaa): ")
                data_nas = datetime.strptime(data_str, "%d-%m-%Y").date()
                cliente = atendente.registrarCliente(nome,cpf,data_nas)
                atendente.adicionar_cliente_venda(cliente)
            else:
                cliente = farmacia.getClientePorCpf(cpf)
                atendente.adicionar_cliente_venda(cliente)
        while True:
                    try:
                        id_produto = int(input("ID do produto (0 para finalizar): "))
                    except ValueError:
                        print(f"{VERMELHO}O ID deve ser um número inteiro.{RESET}")
                        input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                        continue
                    if id_produto == 0:
                        break
                    try:
                        quantidade = int(input("Quantidade: "))
                    except ValueError:
                        print(f"{VERMELHO}A quantidade deve ser um número inteiro.{RESET}")
                        input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                        continue
                    try:
            # busca no estoque
                        if not farmacia._estoque.consultar_produto_por_id(atendente,id_produto):
                            print(f"{AMARELO}Produto não encontrado{RESET}")
                            input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                            continue
                        else:
                            produto, qtd_estoque = farmacia._estoque.consultar_produto_por_id(atendente,id_produto)

                        if quantidade > qtd_estoque:
                            print("Quantidade insuficiente em estoque")
                            input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                            continue

            # adiciona na venda
                        atendente.adicionar_produto_venda(produto,quantidade)
                        print("Produto adicionado à venda!")

                    except ValueError as e:
                        print(f"Erro: {e}")
        atendente.finalizar_venda()
        limpar_tela()
        print(f"{VERDE}ITENS DA VENDA:{RESET}")
        for item in venda.getProdutos():
            print(f'{AZUL}{item}{RESET}')
        print(f"{VERDE}PREÇO TOTAL:{RESET} {AZUL}{venda.getPrecoTotal()}{RESET}")

        if venda.getCliente() is not None:
            print(f"{VERDE}CLIENTE: {venda.getCliente()}{RESET}")
        else:
            print(f"{VERDE}Cliente não adicionado à compra!{RESET}")
  
        input("\nPressione Enter para voltar ao menu...")                 


    def info_gerais():

        limpar_tela()
        print(f"{VERDE}-{RESET}" * 45)
        print(f"{AZUL}|              FICHA DO ATENDENTE             |") 
        print("-" * 45)
        print(f"| {'CAMPO':<15} | {'DADOS':<23} |") # < alinha à esquerda
        print("-" * 45)
        print(f'| {'ID':<15} | {atendente.get_id():<23} |')
        print(f'| {'NOME':<15} | {atendente.nome:<23} |')
        print(f'| {'CPF':<15} | {atendente.get_cpf():<23} |')
        print(f'| {'NASCIMENTO':<15} | {atendente.get_data_nascimento():}               |')
        print(f'| {'SALÁRIO':<15} | {atendente.get_salario_base():<23} |')
        print(f'| {'Nº DE VENDAS ':<15} | {len(atendente.getVendasRealizadas()):<23} |')
        print(f"{VERDE}-{RESET}" * 45)
        input("\nPressione Enter para voltar ao menu...")


# --------------- MENU ----------------
    def menu():

        limpar_tela()
        print(f"{AZUL}=" * 40)
        print(f"{NEGRITO}    Bem Vindo {atendente.nome} {RESET}")
        print(f"{AZUL}=" * 40 + f"{RESET}")

 

       

        print(f"\n{AMARELO}------------------  CAIXA  -------------------{RESET}")
        print(" [1]  Vender Produto")
        print(" [2] Informações Gerais")
        print("-" * 40)
        print(f" {VERMELHO}[0]  Logout{RESET}")
        print("-" * 40)

    while atendente.get_isautenticado():

        menu() 
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
                vender_produto()
        elif opcao == '2':
                info_gerais()
        elif opcao == '0':
                print("\nSaindo do menu... Até logo!")
                time.sleep(1)
                atendente.desautenticar()
                break
        else:
                print("\nOpção inválida!")
                time.sleep(1)
