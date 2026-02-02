from src.utils.tela import limpar_tela , VERDE , AZUL , AMARELO ,VERMELHO ,RESET , NEGRITO
import time
from datetime import datetime
from decimal import Decimal , InvalidOperation
from src.utils.validacoes import *
from src.core.mixins_interfaces import *
from src.farmacia.produto import Produto
#from src.main import login


def iniciar_login_repositor(repositor,farmacia):

# ---------------- PRODUTOS ----------------
    def cadrastar_produto():
        
        while True:

            limpar_tela()
            print("\n--- CADASTRAR NOVO PRODUTO ---")
            nome = input("Nome: ")
            fabricante = input("Fabricante: ")
            try:
                preco = Decimal(input("Preço: "))
                qntd = int(input("Quantidade: "))
            except InvalidOperation:
                print(f"{VERMELHO}Digite um preço válido!{RESET}")
                input("Pressione Enter para tentar novamente...")
                continue 
            except ValueError:
                print(f"{VERMELHO}Quantidade inválida!{RESET}")
                input("Pressione Enter para tentar novamente...")
                continue
            else:
                produto = Produto(nome, preco, fabricante)
                repositor.adicionar_produto_estoque(produto, qntd)
                print(f'{VERDE}Produto cadrastado com sucesso! {RESET}')
                input("\nPressione Enter para voltar ao menu...")
                break


  
        
    def remover_produto():
        while True:
            limpar_tela()
            print("\n--- REMOVER PRODUTO ---")

            try:
                id_produto = int(input("Digite o Id do Produto: "))
                repositor.remover_produto(id_produto)

            except ValueError:
                print(f"{VERMELHO}O ID deve ser um número inteiro.{RESET}")
                input("\nPressione Enter para tentar novamente...")
                continue
            else:
                print(f"{VERDE}Produto removido com sucesso!{RESET}")
                input("\nPressione Enter para voltar ao menu...")
                break

    def alterar_preco_produto():
        while True:
            limpar_tela()
            print("\n--- ALTERAR PREÇO ---")
            try:
                id_produto = int(input("Digite o ID do produto: "))
                novo_preco = Decimal(input("Digite o novo preço: "))     
            except ValueError:
                print(f"{VERMELHO}O ID deve ser um número inteiro.{RESET}")
                input("\nPressione Enter para tentar novamente..")
                continue
            except InvalidOperation:
                print(f"{VERMELHO}Preço inválido{RESET}")
                input("\nPressione Enter para tentar novamente...")
                continue
            else:
                if not repositor.consultar_produto_por_id(id_produto):
                    print(f"{AMARELO}Produto não encontrado{RESET}")
                else:
                    produto , _  = repositor.consultar_produto_por_id(id_produto)
                    repositor.alterar_preco_produto(produto, novo_preco)

                    print(f'{VERDE}Preço alterado com sucesso! {RESET}')
            input("\nPressione Enter para voltar ao menu...")
            break


    def listar_produtos():
        limpar_tela()
        print("\n--- ESTOQUE ATUAL ---")
        if not repositor.consultar_estoque():
            print(f'{AMARELO}Estoque Vazio!{RESET}')
        else:
            print(repositor.consultar_estoque())
        input("\nPressione Enter para voltar ao menu...")


    def buscar_produto():
        while True:
            limpar_tela()
            print("\n--- BUSCAR PRODUTO ---")
            opc = str(input(f"{AZUL}Deseja consultar produto por: (Id)/(Nome) {RESET}"))
            try:
           
                if opc == "Id":
                    id_produto = int(input(f"{AZUL}Digite o Id do Produto: {RESET}"))
                    resultado = repositor.consultar_produto_por_id(id_produto)
                    if resultado is None:
                        print(f"{AMARELO}Produto não encontrado{RESET}")
                        input("\nPressione Enter para voltar ao menu...")
                        break
                    else:
                        print(resultado)
                        input("\nPressione Enter para voltar ao menu...")
                        break
                elif opc == "Nome":
                    nome = str(input(f"{AZUL}Digite o Nome do Produto: {RESET}"))
                    resultado = repositor.consultar_produto_por_nome(nome)
                    if resultado is None:
                        print(f"{AMARELO}Produto não encontrado{RESET}")
                        input("\nPressione Enter para voltar ao menu...")
                        break
                    else:
                        print(resultado)
                        input("\nPressione Enter para voltar ao menu...")
                        break
                else:
                    print(f"{VERMELHO}Opção Incorreta{RESET}")
                    input("\nPressione Enter para tentar novamente...")
                    continue
            except ValueError:
                print(f"{VERMELHO}O ID deve ser um número inteiro.{RESET}")
            input("\nPressione Enter para tentar novamente...")
            continue
                


    def info_gerais():

        limpar_tela()
        print(f"{VERDE}-{RESET}" * 45)
        print(f"{AZUL}|              FICHA DO REPOSITOR             |") 
        print("-" * 45)
        print(f"| {'CAMPO':<15} | {'DADOS':<23} |") # < alinha à esquerda
        print("-" * 45)
        print(f'| {'ID':<15} | {repositor.get_id():<23} |')
        print(f'| {'NOME':<15} | {repositor.nome:<23} |')
        print(f'| {'CPF':<15} | {repositor.get_cpf():<23} |')
        print(f'| {'NASCIMENTO':<15} | {repositor.get_data_nascimento():}               |')
        print(f'| {'SALÁRIO':<15} | {repositor.get_salario_base():<23} |')
        print(f"{VERDE}-{RESET}" * 45)
        input("\nPressione Enter para voltar ao menu...")


# --------------- MENU ----------------
    def menu():

        limpar_tela()
        print(f"{AZUL}=" * 40)
        print(f"{NEGRITO}           Bem Vindo  {repositor.nome} {RESET}")
        print(f"{AZUL}=" * 40 + f"{RESET}")

        print(f"\n{AMARELO}---------------    PRODUTOS  -----------------{RESET}")
        print(" [1]  Cadastrar Produto")
        print(" [2]  Remover Produto")
        print(" [3]  Alterar Preço")
        print(" [4]  Consultar Estoque")
        print(" [5]  Buscar Produto")
        print(" [6] Informações Gerais")
        print(" [7] Logout")
        print("-" * 40)
        print(f" {VERMELHO}[0]  Sair{RESET}")
        print("-" * 40)

    while repositor.get_isautenticado():

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
                buscar_produto()
        elif opcao == '6':
                info_gerais()
        elif opcao == '7':
                repositor.desautenticar()
                break
        elif opcao == '0':
                repositor.desautenticar()
                print("\nSaindo do menu... Até logo!")
                break
        else:
                print("\nOpção inválida!")
                time.sleep(1)
