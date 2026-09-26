import socket
import time

# Configurações de Rede
LOCAL_BRIDGE_IP = "127.0.0.1"
LOCAL_BRIDGE_PORT = 9000   # Porta disponibilizada pela ponte Bluetooth local
PC_IP = "192.168.0.9"      # Endereço IP do Gateway (PC)
UDP_PORT = 1884            # Porta UDP do Gateway MQTT-SN

# Instanciação do socket UDP para encaminhamento de pacotes
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[FORWARDER] Tentando conectar à ponte local em {LOCAL_BRIDGE_IP}:{LOCAL_BRIDGE_PORT}...")

# Aguarda a inicialização do serviço de bridge Bluetooth
while True:
    try:
        tcp_bridge = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_bridge.connect((LOCAL_BRIDGE_IP, LOCAL_BRIDGE_PORT))
        print("[FORWARDER] Conectado com sucesso à ponte do app!")
        break
    except ConnectionRefusedError:
        print("[FORWARDER] Aguardando o app BT/TCP Bridge iniciar no Celular 2 (porta 9000)...")
        time.sleep(2)

try:
    while True:
        # Leitura dos bytes brutos recebidos via Bluetooth
        data = tcp_bridge.recv(1024)
        if not data:
            print("[FORWARDER] Conexão encerrada pelo cliente.")
            break
        
        print(f"[FORWARDER] {len(data)} bytes recebidos via Bluetooth -> Encaminhando UDP para {PC_IP}:{UDP_PORT}")
        
        # Envio transparente do pacote MQTT-SN ao Gateway
        udp_sock.sendto(data, (PC_IP, UDP_PORT))

except Exception as e:
    print(f"[FORWARDER] Erro de execução: {e}")
finally:
    tcp_bridge.close()
    udp_sock.close()
    print("[FORWARDER] Encaminhador finalizado.")