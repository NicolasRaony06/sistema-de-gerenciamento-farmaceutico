# ---------------- IMPORTS ----------------
import os
import time
from datetime import datetime
from decimal import Decimal , InvalidOperation

from src.core.atendente import Atendente
from src.core.cliente import Cliente
from src.core.funcionario import Funcionario
from src.core.gerente import Gerente
from src.core.pessoa import Pessoa
from src.utils.validacoes import *
from src.core.mixins_interfaces import *

from src.farmacia.farmacia import Farmacia
from src.farmacia.estoque import Estoque
from src.farmacia.produto import Produto
from src.farmacia.venda import Venda
# ----------------------------------------
def limpar_tela():
        """Limpa o console."""
        os.system('cls' if os.name == 'nt' else 'clear')   
# CORES
VERDE = '\033[92m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'
NEGRITO = '\033[1m'
# ------------------
#----------------------------------------
def login():
    limpar_tela()
    print("=" * 40)
    print("                 LOGIN     ")
    print("=" * 40)
    
    id_login = int(input("Digite seu Id: "))
    senha_login = input("Digite sua senha para login: ")

    usuario_encontrado = None

    # Verifica se é o Gerente Principal (Global)
    if 'gerente' in globals() and gerente.get_id() == id_login:
        usuario_encontrado = gerente
    # Se não, busca na lista de funcionários da farmácia
    else:
        usuario_encontrado = farmacia.getFuncionarioPorId(id_login)

    if usuario_encontrado:
        
            # Tenta autenticar o usuário encontrado (seja Gerente ou Atendente)
            usuario_encontrado.setAutenticacao(id_login, senha_login)
            
            if usuario_encontrado.get_isautenticado():
                if isinstance(usuario_encontrado, Gerente):
                    iniciar_login_gerente(usuario_encontrado, farmacia)
                elif isinstance(usuario_encontrado, Atendente):
                    iniciar_login_atendente(usuario_encontrado, farmacia)
                else:
                    print(f"{AMARELO}Usuário sem menu definido.{RESET}")
            else:
                print(f"{VERMELHO}Senha incorreta!{RESET}")
                time.sleep(2)
        
    else:
        print(f"{VERMELHO}Usuário não encontrado!{RESET}")
        time.sleep(2)

limpar_tela()
farmacia = Farmacia("Farmacia Holanda")
def iniciar_login_atendente(atendente,farmacia):

# ---------------- PRODUTOS ----------------
    def cadrastar_produto():
        limpar_tela()
        print("\n--- CADASTRAR NOVO PRODUTO ---")
        nome = str(input("Nome: "))
        qntd = int(input("Quantidade: "))
        fabricante = str(input("Fabricante: "))
        try:
            preco = Decimal(input("Preço: "))
        except Decimal.ConversionSyntax:
            print("Digite um preço válido!")
            cadrastar_produto()    
            

        produto = Produto(nome, preco, fabricante)
        atendente.adicionar_produto_estoque(produto, qntd)

        print(f'{VERDE}Produto cadrastado com sucesso! {RESET}')
        
        input("\nPressione Enter para voltar ao menu...")


    def remover_produto():
        limpar_tela()
        print("\n--- REMOVER PRODUTO ---")
        id_produto = int(input("Digite o Id do Produto: "))
        atendente.remover_produto(id_produto) 
        print(f'{VERDE}Produto removido com sucesso! {RESET}')
        input("\nPressione Enter para voltar ao menu...")


    def alterar_preco_produto():
        limpar_tela()
        print("\n--- ALTERAR PREÇO ---")
        id_produto = int(input("Digite o ID do produto: "))
        novo_preco = Decimal(input("Digite o novo preço: "))

        produto , _ = atendente.consultar_produto_por_id(id_produto)
        atendente.alterar_preco_produto(produto, novo_preco)
        print(f'{VERDE}Preço alterado  com sucesso! {RESET}')
        input("\nPressione Enter para voltar ao menu...")


    def listar_produtos():
        limpar_tela()
        print("\n--- ESTOQUE ATUAL ---")
        if not atendente.consultar_estoque():
            print(f'{AMARELO}Estoque Vazio!{RESET}')
        else:
            print(atendente.consultar_estoque())

        input("\nPressione Enter para voltar ao menu...")


    def buscar_produto():
        limpar_tela()
        print("\n--- BUSCAR PRODUTO ---")
        opc = input(f"{AZUL}Deseja consultar produto por: (Id)/(Nome) {RESET}")
        if opc == "Id":
            id_produto = int(input(f"{AZUL}Digite o Id do Produto: {RESET}"))

            resultado = atendente.consultar_produto_por_id(id_produto)
            if resultado is None:
                print(f"{AMARELO}Produto não encontrado{RESET}")
            else:
                print(resultado)
        elif opc == "Nome":
            nome = input(f"{AZUL}Digite o Nome do Produto: {RESET}")
            resultado = atendente.consultar_produto_por_nome(nome)
            if resultado is None:
                print(f"{AMARELO}Produto não encontrado{RESET}")
            else:
                print(resultado)
        else:
            print(f"{VERMELHO}Opção Incorreta{RESET}")
        input("\nPressione Enter para voltar ao menu...")



# ---------------- FUNCIONÁRIOS ----------------




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
            id_produto = int(input("ID do produto (0 para finalizar): "))

            if id_produto == 0:
                break

            quantidade = int(input("Quantidade: "))
        
            try:
            # busca no estoque
                produto, qtd_estoque = atendente.consultar_produto_por_id(id_produto)

                if quantidade > qtd_estoque:
                    print("Quantidade insuficiente em estoque")
                    continue

            # adiciona na venda
                atendente.adicionar_produto_venda(produto,quantidade)


                print("Produto adicionado à venda!")

            except ValueError as e:
                print(f"Erro: {e}")

        atendente.finalizar_venda()
        print(f"{VERDE}ITENS DA VENDA:{RESET}")
        for item in venda.getProdutos():
            print(item)
        print(f"{VERDE}PREÇO TOTAL: {venda.getPrecoTotal()}{RESET}")

        if venda.getCliente() is not None:
            print(f"{VERDE}CLIENTE: {venda.getCliente()}{RESET}")
        else:
            print(f"{VERDE}Cliente não adicionado à compra!{RESET}")

        input("\nPressione Enter para voltar ao menu...")

    def info_gerais():

        limpar_tela()
        print("-" * 45)
        print(f"|              FICHA DO ATENDENTE             |") 
        print("-" * 45)
        print(f"| {'CAMPO':<15} | {'DADOS':<23} |") # < alinha à esquerda
        print("-" * 45)
        print(f'| {'ID':<15} | {atendente.get_id():<23} |')
        print(f'| {'NOME':<15} | {atendente.nome:<23} |')
        print(f'| {'CPF':<15} | {atendente.get_cpf():<23} |')
        print(f'| {'NASCIMENTO':<15} | {atendente.get_data_nascimento():}              |')
        print(f'| {'SALÁRIO':<15} | {atendente.get_salario_base():<23} |')
        print(f'| {'NÚMERO DE VENDAS':<15}| {len(atendente.getVendasRealizadas()):<23} |')
        print("-" * 45)
        input("\nPressione Enter para voltar ao menu...")


# --------------- MENU ----------------
    def menu2():

        limpar_tela()
        print(f"{AZUL}=" * 40)
        print(f"{NEGRITO}         SISTEMA DE FARMÁCIA v1.0  {RESET}")
        print(f"{AZUL}=" * 40 + f"{RESET}")

        print(f"\n{AMARELO}---------------    PRODUTOS  -----------------{RESET}")
        print(" [1]  Cadastrar Produto")
        print(" [2]  Remover Produto")
        print(" [3]  Alterar Preço")
        print(" [4]  Consultar Estoque")
        print(" [5]  Buscar Produto")

        print(f"\n{AMARELO}------------------  CAIXA  -------------------{RESET}")
        print(" [6]  Vender Produto")
        print(" [7] Informações Gerais")
        print(" [8] Logout")
        print("-" * 40)
        print(f" {VERMELHO}[0]  Sair{RESET}")
        print("-" * 40)

    while atendente.get_isautenticado():

        menu2() 
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
                vender_produto()
        elif opcao == '7':
                info_gerais()
        elif opcao == '8':
                login()     
        elif opcao == '0':
                atendente.desautenticar()
                print("\nSaindo do menu... Até logo!")
                break
        else:
                print("\nOpção inválida!")
                time.sleep(1)


def iniciar_login_gerente(gerente,farmacia):

# ---------------- PRODUTOS ----------------
    def cadrastar_produto():
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
            return cadrastar_produto()
        except ValueError:
            print(f"{VERMELHO}Quantidade inválida!{RESET}")
            input("Pressione Enter para tentar novamente...")
            return cadrastar_produto()
        else:
            produto = Produto(nome, preco, fabricante)
            gerente.adicionar_produto_estoque(produto, qntd)
            print(f'{VERDE}Produto cadrastado com sucesso! {RESET}')
            input("\nPressione Enter para voltar ao menu...")


  
        
    def remover_produto():
        limpar_tela()
        print("\n--- REMOVER PRODUTO ---")

        try:
            id_produto = int(input("Digite o Id do Produto: "))
            sucesso = gerente.remover_produto(id_produto)

            if sucesso:
                print("Produto removido com sucesso!")
            else:
                print("Erro: produto não encontrado.")

        except ValueError:
            print("Erro: o ID deve ser um número inteiro.")

        
        input("\nPressione Enter para voltar ao menu...")

    def alterar_preco_produto():
        limpar_tela()
        try:
            print("\n--- ALTERAR PREÇO ---")
            id_produto = int(input("Digite o ID do produto: "))
            novo_preco = Decimal(input("Digite o novo preço: "))

            produto , _ = gerente.consultar_produto_por_id(id_produto)
            gerente.alterar_preco_produto(produto, novo_preco)
        except Exception as erro:
            print(f"{VERMELHO}Erro: {erro} Tente Novamente.....{RESET}")
        else:
            print(f'{VERDE}Preço alterado  com sucesso! {RESET}')
            input("\nPressione Enter para voltar ao menu...")


    def listar_produtos():
        limpar_tela()
        try:
            print("\n--- ESTOQUE ATUAL ---")
            if not gerente.consultar_estoque():
                print(f'{AMARELO}Estoque Vazio!{RESET}')
            else:
                print(gerente.consultar_estoque())
        except Exception as erro:
            print(f"{VERMELHO}Erro: {erro} Tente Novamente.....{RESET}")
        else:
            input("\nPressione Enter para voltar ao menu...")


    def buscar_produto():
        limpar_tela()
        print("\n--- BUSCAR PRODUTO ---")
        opc = input(f"{AZUL}Deseja consultar produto por: (Id)/(Nome) {RESET}")
        if opc == "Id":
            id_produto = int(input(f"{AZUL}Digite o Id do Produto: {RESET}"))

            resultado = gerente.consultar_produto_por_id(id_produto)
            if resultado is None:
                print(f"{AMARELO}Produto não encontrado{RESET}")
            else:
                print(resultado)
        elif opc == "Nome":
            nome = input(f"{AZUL}Digite o Nome do Produto: {RESET}")
            resultado = gerente.consultar_produto_por_nome(nome)
            if resultado is None:
                print(f"{AMARELO}Produto não encontrado{RESET}")
            else:
                print(resultado)
        else:
            print(f"{VERMELHO}Opção Incorreta{RESET}")
        input("\nPressione Enter para voltar ao menu...")



# ---------------- FUNCIONÁRIOS ----------------
    def cadrastar_funcionario():
        limpar_tela()
        print("\n--- CADASTRAR FUNCIONÁRIO ---")
        nome = input(f"{AZUL}Digite o nome do funcionário: {RESET}")
        cpf = input(f"{AZUL}Digite o CPF do funcionário: {RESET}")

        data_str = input(f"{AZUL}Data de nascimento (dd-mm-aaaa): {RESET}")
        data_nascimento = datetime.strptime(data_str, "%d-%m-%Y").date()

        salario = Decimal(input(f"{AZUL}Salário do funcionário: {RESET}"))
        cargo = str(input(f"{AZUL}Digite o cargo do funcionário: (atendente/repositor): {RESET}"))
        g = gerente.cadrastar_funcionario(cargo,nome, cpf, data_nascimento, salario)

        print(f"{VERDE}Funcionário {g.nome}, com Id: {g.get_id()} cadastrado{RESET}")
        input("\nPressione Enter para voltar ao menu...")


    def excluir_funcionario():
        limpar_tela()
        print("\n--- EXCLUIR FUNCIONÁRIO ---")
        id_funcionario = int(input("Digite o Id do funcionário: "))

        funcionario = gerente.getFarmacia().getFuncionarioPorId(id_funcionario)
        gerente.excluir_funcionario(funcionario)
        print(f"{VERDE}Funcionário excluido!{RESET}")
        input("\nPressione Enter para voltar ao menu...")


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
        print(f"{VERDE}ITENS DA VENDA:{RESET}")
        for item in venda.getProdutos():
            print(item)
        print(f"{VERDE}PREÇO TOTAL: {venda.getPrecoTotal()}{RESET}")

        if venda.getCliente() is not None:
            print(f"{VERDE}CLIENTE: {venda.getCliente()}{RESET}")
        else:
            print(f"{VERDE}Cliente não adicionado à compra!{RESET}")

        input("\nPressione Enter para voltar ao menu...")

    def info_gerais():

        limpar_tela()
        print("-" * 45)
        print(f"|              FICHA DO GERENTE             |") 
        print("-" * 45)
        print(f"| {'CAMPO':<15} | {'DADOS':<23} |") # < alinha à esquerda
        print("-" * 45)
        print(f'| {'ID':<15} | {gerente.get_id():<23} |')
        print(f'| {'NOME':<15} | {gerente.nome:<23} |')
        print(f'| {'CPF':<15} | {gerente.get_cpf():<23} |')
        print(f'| {'NASCIMENTO':<15} | {gerente.get_data_nascimento():}              |')
        print(f'| {'SALÁRIO':<15} | {gerente.get_salario_base():<23} |')
        print(f'| {'NÚMERO DE VENDAS':<15}| {len(gerente.getVendasRealizadas()):<23} |')
        print("-" * 45)
        input("\nPressione Enter para voltar ao menu...")


# --------------- MENU ----------------
    def menu():

        limpar_tela()
        print(f"{AZUL}=" * 40)
        print(f"{NEGRITO}         SISTEMA DE FARMÁCIA v1.0  {RESET}")
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
             login()
        elif opcao == '0':
                gerente.desautenticar()
                print("\nSaindo do menu... Até logo!")
                break
        else:
                print("\nOpção inválida!")
                time.sleep(1)



# ---------------- PONTO DE ENTRADA ----------------
if __name__ == "__main__":
        

        while True:
            limpar_tela()
            print("=" * 40)
            print("     SISTEMA FARMÁCIA HOLANDA")
            print("=" * 40)
            print("\n[1] Entrar no sistema (Cadastrar/Login Gerente)")
            print("[0] Encerrar Programa")
            opc = input("\nEscolha uma opção: ")

            if opc == "0":
                print("\nEncerrando sistema... Até logo!")
                break # Sai do loop principal e termina o programa

            if opc == "1":
                limpar_tela()
    
            
            # Nota: No seu código original, você cadastra um NOVO gerente toda vez que entra.
        
                print("\n--- CADASTRO DO GERENTE ---")
                
                nome = input("Digite o Nome do Gerente: ")
                while True:
                    try:
                        cpf = input("Digite o CPF: ")
                        cpf = validar_formato_cpf(cpf)
                        break
                    except  ValueError as e:
                        print(f"{VERMELHO}{e}{RESET}")
                        input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                        
                while True:
                    try:
                        data_str = input("Data de nascimento (dd-mm-aaaa): ")
                        data_nascimento = datetime.strptime(data_str, "%d-%m-%Y").date()
                        break
                    except ValueError:
                        print(f"{VERMELHO}Data inválida! Use o formato dd-mm-aaaa.{RESET}")
                        input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                        
                while True:
                    try:
                        salario = Decimal(input("Salário: "))
                        break
                    except InvalidOperation:
                        print(f"{VERMELHO}Salário inválido.{RESET}")
                        input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                        
                while True:
                    try:
                        senha = input("Digite a senha de login: ")
                        break
                    except ValueError:
                        print(f"{VERMELHO}Senha inválida!.{RESET}")
                        input(f"{AZUL}Pressione Enter para tentar novamente...{RESET}")
                       

                gerente = farmacia._registrarGerente(
                    nome, cpf, data_nascimento, salario, senha
                )

                print(f"\n✔ Gerente cadastrado com sucesso, com Id:{gerente.get_id()}")
                time.sleep(1)
                    
                login()
