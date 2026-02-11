import socket
from colorama import init, Fore, Style

# Inicializa o colorama para que as cores funcionem no Windows
init()

def scan_ports(alvo, portas):
    """
    Função principal que realiza a varredura de portas.
    """
    print(f"\n{Fore.CYAN}[*] Iniciando varredura no alvo: {alvo}{Style.RESET_ALL}")
    print("-" * 40)
    
    # Loop que passa por cada porta da nossa lista
    for porta in portas:
        # Criamos o socket (o "conector" de rede)
        # AF_INET = IPv4 | SOCK_STREAM = TCP
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Define um tempo limite (timeout) de 0.5 segundos
        # Se demorar mais que isso, o script não trava e pula para a próxima
        cliente_socket.settimeout(0.5)
        
        # AQUI A MÁGICA ACONTECE:
        # connect_ex retorna 0 se a conexão for sucesso (Porta Aberta)
        codigo_retorno = cliente_socket.connect_ex((alvo, porta))
        
        if codigo_retorno == 0:
            # Se a porta estiver aberta, pintamos de VERDE
            print(f"{Fore.GREEN}[+] Porta {porta}: ABERTA{Style.RESET_ALL}")
        else:
            # Se fechada, pintamos de VERMELHO (opcional, mas bom para visualizar)
            print(f"{Fore.RED}[-] Porta {porta}: FECHADA{Style.RESET_ALL}")
            
        # Fechamos o conector para liberar memória
        cliente_socket.close()
    
    print("-" * 40)
    print(f"{Fore.CYAN}[*] Scan finalizado.{Style.RESET_ALL}")

if __name__ == "__main__":
    # Definição do alvo (localhost é sua própria máquina)
    alvo = 'localhost' 
    
    # Lista de portas comuns para verificar:
    # 21(FTP), 22(SSH), 80(HTTP), 443(HTTPS), 3306(MySQL), 8080(Alt Web)
    portas_comuns = [21, 22, 25, 80, 443, 3306, 8080]
    
    try:
        scan_ports(alvo, portas_comuns)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Operação interrompida pelo usuário.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Erro inesperado: {e}{Style.RESET_ALL}")
