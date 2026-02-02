import os
# Cores 
VERDE = '\033[92m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'
NEGRITO = '\033[1m'
def limpar_tela():
        """Limpa o console."""
        os.system('cls' if os.name == 'nt' else 'clear')   