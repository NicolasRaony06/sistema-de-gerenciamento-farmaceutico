# ---------------- IMPORTS ----------------
from src.utils.tela import limpar_tela , VERDE , AZUL , AMARELO ,VERMELHO ,RESET , NEGRITO
import time
from datetime import datetime
from decimal import Decimal , InvalidOperation
from src.utils.validacoes import *
from src.farmacia.farmacia import Farmacia
from src.core.gerente import Gerente
from src.core.atendente import Atendente
from src.core.repositor import Repositor
from src.ui.menu_atendente import iniciar_login_atendente
from src.ui.menu_gerente import iniciar_login_gerente
from src.ui.menu_repositor import iniciar_login_repositor
#Funcao login
def login(farmacia):
    
    limpar_tela()
    print("=" * 40)
    print("                 LOGIN     ")
    print("=" * 40)
    while True:
        try:
            id_login = int(input("Digite seu Id: "))
        except ValueError:
            print(f"{VERMELHO}Id inválido{RESET}")
            continue
        senha_login = input("Digite sua senha para login: ")
        usuario_encontrado = None

    # Verifica se é o Gerente Principal (Global)
        if gerente.get_id() == id_login:
            usuario_encontrado = gerente
    # Se não, busca na lista de funcionários da farmácia
        else:
            usuario_encontrado = farmacia.getFuncionarioPorId(id_login)

        if not usuario_encontrado:
            print(f"{VERMELHO}Usuário não encontrado!{RESET}")
            continue 
        try:
            usuario_encontrado.setAutenticacao(id_login,senha_login)
        except ValueError:
            print(f"{VERMELHO}Senha incorreta{RESET}")
            continue
        
            
        return usuario_encontrado

Farmacia = Farmacia('HOLANDA')
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
                       

                gerente = Farmacia._registrarGerente(
                    nome, cpf, data_nascimento, salario, senha
                )

                print(f"{VERDE}Gerente cadastrado com sucesso, com Id:{gerente.get_id()}{RESET}")
                time.sleep(1)
                    
                while True: 
                    # 1. Chama o Login
                    usuario_logado = login(Farmacia)
                    
   
                    if usuario_logado is None:
                        break 

                    # 3. Verifica se logou e chama o menu correspondente
                    if usuario_logado.get_isautenticado():
                        if isinstance(usuario_logado,Gerente):
                            iniciar_login_gerente(usuario_logado, Farmacia)
                        elif isinstance(usuario_logado,Atendente):
                            iniciar_login_atendente(usuario_logado,Farmacia)
                        elif isinstance(usuario_logado,Repositor):
                            iniciar_login_repositor(usuario_logado,Farmacia)
                        
                    else:
                        print(f"{VERMELHO}Erro de autenticação.{RESET}")