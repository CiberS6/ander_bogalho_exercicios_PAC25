import socket
import threading

HOST = '127.0.0.1'
PORT = 12340

def receive_messages(client_socket):
    """Thread para receber mensagens do servidor."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message, end='')
            else:
                break
        except:
            print("\n[Erro] Conexão perdida com o servidor.")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((HOST, PORT))
        print("Conectado ao servidor GDPR Chat!")
        
        # Thread para receber mensagens
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()

        # Loop de envio
        while True:
            message = input("")
            if message.lower() == 'exit':
                client_socket.send("exit".encode('utf-8'))
                break
            
            if message.strip():
                client_socket.send(message.encode('utf-8'))
                
    except ConnectionRefusedError:
        print("Erro: Servidor não está ligado. Inicie o server.py primeiro.")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        client_socket.close()
        print("Desconectado.")

if __name__ == "__main__":
    main()