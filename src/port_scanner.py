# Primeiro, avisamos ao Python que vamos usar ferramentas para conexão de rede.
# A biblioteca 'socket' é a caixa de ferramentas padrão para isso.
import socket
# Agora, definimos o alvo que nosso programa vai escanear.
# 'localhost' é um nome especial para o SEU PRÓPRIO COMPUTADOR.
# É 100% seguro escanear a si mesmo para aprender.
alvo = 'localhost'

# Apenas uma linha para deixar a saída do programa mais organizada.
print(f"[*] Escaneando o alvo: {alvo}")
print("-" * 30)
# Usamos um bloco 'try...except' por segurança.
# Ele tenta executar o código dentro do 'try'. Se der algum erro (ex: sem internet),
# ele pula para o 'except' e mostra uma mensagem amigável, em vez de travar.
try:
    # Criamos uma lista com as portas mais comuns que queremos testar.
    # 80 é para web (HTTP), 443 para web segura (HTTPS), 22 para acesso remoto (SSH), etc.
    portas_comuns = [21, 22, 25, 80, 443, 3306, 8080]

    # Agora, criamos um loop que vai passar por cada número da nossa lista.
    for porta in portas_comuns:
        # Para cada porta, criamos um novo "conector" (socket).
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Definimos um tempo limite de 1 segundo. Se a porta não responder,
        # o programa não fica travado esperando para sempre. Ele desiste e passa para a próxima.
        cliente_socket.settimeout(1)
        
        # AQUI A MÁGICA ACONTECE:
        # O programa tenta se conectar ao 'alvo' na 'porta' da vez.
        resultado = cliente_socket.connect_ex((alvo, porta))
        
        # Verificamos o resultado. Se for 0, significa SUCESSO! A porta está aberta.
        if resultado == 0:
            print(f"[+] Porta {porta}: ABERTA")
        # Se o resultado for outro número, significa que a porta está fechada e não fazemos nada.
        
        # Fechamos o "conector" para liberar recursos do computador.
        cliente_socket.close()
        # Caso algum erro tenha acontecido lá no começo, esta parte avisa o usuário.
except Exception as e:
    print(f"[!] Ocorreu um erro inesperado: {e}")

# Mensagem final para sabermos que o programa terminou seu trabalho.
print("-" * 30)
print("[*] Scan finalizado.")
