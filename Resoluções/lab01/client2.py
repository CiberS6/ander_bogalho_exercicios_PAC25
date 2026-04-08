import socket
import threading
import sys
import time

HOST = '127.0.0.1'
PORT = 12340

def receive_messages(client_socket):
    """Thread que recebe mensagens do servidor em tempo real."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Limpa a linha atual de input e imprime a mensagem
                print('\r' + ' ' * 80 + '\r', end='')  # limpa a linha
                print(message, end='')
                # Volta a mostrar o prompt de input
                print("\n> ", end='', flush=True)
            else:
                break
        except:
            print("\n[Erro] Conexão perdida com o servidor.")
            break


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((HOST, PORT))
        print("Conectado ao servidor GDPR Chat!\n")
        
        # Inicia a thread de receção
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()

        # Loop principal para envio de mensagens
        print("> ", end='', flush=True)
        while True:
            message = input()
            if message.lower() == 'exit':
                client_socket.send("exit".encode('utf-8'))
                break
            
            if message.strip():
                client_socket.send(message.encode('utf-8'))
                print("> ", end='', flush=True)   # volta a mostrar o prompt

    except ConnectionRefusedError:
        print("Erro: O servidor não está a correr. Inicie primeiro o server.py")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        client_socket.close()
        print("\nDesconectado do servidor.")


if __name__ == "__main__":
    main()