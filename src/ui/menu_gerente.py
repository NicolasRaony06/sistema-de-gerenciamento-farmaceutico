from src.utils.tela import limpar_tela , VERDE , AZUL , AMARELO ,VERMELHO ,RESET , NEGRITO
import time
from datetime import datetime
from decimal import Decimal , InvalidOperation
from src.utils.validacoes import *
from src.core.mixins_interfaces import *
from src.farmacia.produto import Produto

#from src.main import login
def iniciar_login_gerente(gerente,farmacia):

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
                gerente.adicionar_produto_estoque(produto, qntd)
                print(f'{VERDE}Produto cadrastado com sucesso! {RESET}')
                input("\nPressione Enter para voltar ao menu...")
                break


  
        
    def remover_produto():
        while True:
            limpar_tela()
            print("\n--- REMOVER PRODUTO ---")

            try:
                id_produto = int(input("Digite o Id do Produto: "))
                gerente.remover_produto(id_produto)

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
                if not gerente.consultar_produto_por_id(id_produto):
                    print(f"{AMARELO}Produto não encontrado{RESET}")
                else:
                    produto , _  = gerente.consultar_produto_por_id(id_produto)
                    gerente.alterar_preco_produto(produto, novo_preco)

                    print(f'{VERDE}Preço alterado com sucesso! {RESET}')
            input("\nPressione Enter para voltar ao menu...")
            break


    def listar_produtos():
        limpar_tela()
        print("\n--- ESTOQUE ATUAL ---")
        if not gerente.consultar_estoque():
            print(f'{AMARELO}Estoque Vazio!{RESET}')
        else:
            print(gerente.consultar_estoque())
        input("\nPressione Enter para voltar ao menu...")


    def buscar_produto():
        while True:
            limpar_tela()
            print("\n--- BUSCAR PRODUTO ---")
            opc = str(input(f"{AZUL}Deseja consultar produto por: (Id)/(Nome) {RESET}"))
            try:
           
                if opc == "Id":
                    id_produto = int(input(f"{AZUL}Digite o Id do Produto: {RESET}"))
                    resultado = gerente.consultar_produto_por_id(id_produto)
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
                    resultado = gerente.consultar_produto_por_nome(nome)
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
                

        



# ---------------- FUNCIONÁRIOS ----------------
    def cadrastar_funcionario():
        while True:
            limpar_tela()
            print("\n--- CADASTRAR FUNCIONÁRIO ---")
            nome = input(f"{AZUL}Digite o nome do funcionário: {RESET}") 
            cargo = str(input(f"{AZUL}Digite o cargo do funcionário: (Atendente/Repositor): {RESET}"))
            if cargo != "Atendente" and cargo != "Repositor":
                print(f"{VERMELHO}Opção inválida.{RESET}")
                input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                continue

            try:
                cpf = input(f"{AZUL}Digite o CPF do funcionário: {RESET}")
                validar_formato_cpf(cpf)
            except Exception as erro:
                print(f"{erro}")
                input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                continue

            try:
                data_str = input(f"{AZUL}Data de nascimento (dd-mm-aaaa): {RESET}")
                data_nascimento = datetime.strptime(data_str, "%d-%m-%Y").date()
            except ValueError:
                print(f"{VERMELHO}Data inválida! Use o formato dd-mm-aaaa.{RESET}")
                input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                continue
            try:
    
                salario = Decimal(input(f"{AZUL}Salário do funcionário: {RESET}"))
            except InvalidOperation:
                print(f"{VERMELHO}Valor inválido.{RESET}")
                input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                continue
            else:
                g = gerente.cadrastar_funcionario(cargo,nome, cpf, data_nascimento, salario)
        
                print(f"{VERDE}Funcionário {g.nome}, com Id: {g.get_id()} cadastrado{RESET}")
            
                input("\nPressione Enter para voltar ao menu...")
                break

    def excluir_funcionario():
        while True:
            limpar_tela()
            print("\n--- EXCLUIR FUNCIONÁRIO ---")
            try:
                id_funcionario = int(input("Digite o Id do funcionário: "))
            except ValueError:
                print(f"{VERMELHO}O ID deve ser um número inteiro.{RESET}")
                input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                continue
            else:
                if not gerente.getFarmacia().getFuncionarioPorId(id_funcionario):
                    print(f"{AMARELO}Funcionário não encontrado.{RESET}")
                else:
                    funcionario = gerente.getFarmacia().getFuncionarioPorId(id_funcionario)
                    gerente.excluir_funcionario(funcionario)
                    print(f"{VERDE}Funcionário excluido!{RESET}")
                    
            input("\nPressione Enter para voltar ao menu...")
            break

    def listar_funcionarios():
        limpar_tela()
        print("\n--- LISTA DE FUNCIONÁRIOS ---")
        if not gerente.consultar_lista_funcionario():
            print(f'{AMARELO}Sem funcionários cadrastados!{RESET}')
        else:
            print(gerente.consultar_lista_funcionario())

        input("\nPressione Enter para voltar ao menu...")
        


# ---------------- VENDAS ----------------
    def vender_produto():
        limpar_tela()
        venda = gerente.registrar_venda()
        opc_cliente = input("Deseja Adicionar Cliente a Venda?(S/N) ")
        if opc_cliente == 'S':
            cpf = str(input("Digite o Cpf do cliente: "))
            if not farmacia.getClientePorCpf(cpf):
                print("Cliente não cadrastado no sistema!")
                nome = str(input("Nome do cliente: "))
                data_str = input("Data de nascimento (dd-mm-aaaa): ")
                data_nas = datetime.strptime(data_str, "%d-%m-%Y").date()
                cliente = gerente.registrarCliente(nome,cpf,data_nas)
                gerente.adicionar_cliente_venda(cliente)
            else:
                cliente = farmacia.getClientePorCpf(cpf)
                gerente.adicionar_cliente_venda(cliente)
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
                        if not gerente.consultar_produto_por_id(id_produto):
                            print(f"{AMARELO}Produto não encontrado{RESET}")
                            input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                            continue
                        else:
                            produto, qtd_estoque = gerente.consultar_produto_por_id(id_produto)

                        if quantidade > qtd_estoque:
                            print("Quantidade insuficiente em estoque")
                            input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                            continue

            # adiciona na venda
                        gerente.adicionar_produto_venda(produto,quantidade)
                        print("Produto adicionado à venda!")

                    except ValueError as e:
                        print(f"Erro: {e}")

        gerente.finalizar_venda()
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
        print(f"{AZUL}|              FICHA DO GERENTE             |") 
        print("-" * 45)
        print(f"| {'CAMPO':<15} | {'DADOS':<23} |") # < alinha à esquerda
        print("-" * 45)
        print(f'| {'ID':<15} | {gerente.get_id():<23} |')
        print(f'| {'NOME':<15} | {gerente.nome:<23} |')
        print(f'| {'CPF':<15} | {gerente.get_cpf():<23} |')
        print(f'| {'NASCIMENTO':<15} | {gerente.get_data_nascimento():}               |')
        print(f'| {'SALÁRIO':<15} | {gerente.get_salario_base():<23} |')
        print(f'| {'Nº DE VENDAS ':<15} | {len(gerente.getVendasRealizadas()):<23} |')
        print(f"{VERDE}-{RESET}" * 45)
        input("\nPressione Enter para voltar ao menu...")


# --------------- MENU ----------------
    def menu():

        limpar_tela()
        print(f"{AZUL}=" * 40)
        print(f"{NEGRITO}    Bem Vindo {gerente.nome} {RESET}")
        print(f"{AZUL}=" * 40 + f"{RESET}")

        print(f"\n{AMARELO}---------------    PRODUTOS  -----------------{RESET}")
        print(" [1]  Cadastrar Produto")
        print(" [2]  Remover Produto")
        print(" [3]  Alterar Preço")
        print(" [4]  Consultar Estoque")
        print(" [5]  Buscar Produto")

        print(f"\n{AMARELO}---------------  FUNCIONÁRIOS  --------------- {RESET}")
        print(" [6]  Cadastrar Funcionário")
        print(" [7]  Excluir Funcionário")
        print(" [8]  Listar Funcionários")

        print(f"\n{AMARELO}------------------  CAIXA  -------------------{RESET}")
        print(" [9]  Vender Produto")
        print(" [10] Informações Gerais")
        print(" [11] Logout")
        print("-" * 40)
        print(f" {VERMELHO}[0]  Sair{RESET}")
        print("-" * 40)

    while gerente.get_isautenticado():

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
                cadrastar_funcionario()
        elif opcao == '7':
                excluir_funcionario()
        elif opcao == '8':
                listar_funcionarios()
        elif opcao == '9':
                vender_produto()
        elif opcao == '10':
                info_gerais()
        elif opcao == '11':
            gerente.desautenticar()
            break
        elif opcao == '0':
                gerente.desautenticar()
                print("\nSaindo do menu... Até logo!")
                break
        else:
                print("\nOpção inválida!")
                time.sleep(1)

