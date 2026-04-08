import socket
import threading
import re
import os
from datetime import datetime

HOST = '127.0.0.1'
PORT = 12340

DATA_FOLDER = "Resoluções/lab01/registros"
DATA_FILE = os.path.join(DATA_FOLDER, "dados.txt")

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

clients = {}
clients_lock = threading.Lock()

PERSONAL_DATA_PATTERNS = {
    "Email": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
    "Telefone (PT/Internacional)": re.compile(r'(?:\+351)?[9][1236]\d{7}|\+?\d{1,4}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'),
    "IP Address": re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'),
    "Nome Completo": re.compile(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+){1,3}\b'),
    "Data de Nascimento": re.compile(r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b'),
    "Cartão de Crédito": re.compile(r'\b(?:\d{4}[- ]?){3}\d{4}\b')
}

def detect_personal_data(message):
    found = []
    for data_type, pattern in PERSONAL_DATA_PATTERNS.items():
        if pattern.search(message):
            found.append(data_type)
    return found

def save_personal_data(username, message, detected_types):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Usuário: {username}\n")
        f.write(f"Tipos detetados: {', '.join(detected_types)}\n")
        f.write(f"Mensagem: {message}\n")
        f.write("-" * 80 + "\n\n")

def broadcast(message, sender_socket=None):
    with clients_lock:
        for client_socket in list(clients.keys()):
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode('utf-8'))
                except:
                    remove_client(client_socket)

def remove_client(client_socket):
    with clients_lock:
        if client_socket in clients:
            username = clients[client_socket]
            del clients[client_socket]
            client_socket.close()
            broadcast(f"\n[Servidor] {username} saiu do chat.\n")

def handle_client(client_socket, address):
    try:
        client_socket.send("Digite o seu username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8').strip()
        
        with clients_lock:
            clients[client_socket] = username
        
        print(f"Novo cliente conectado: {username} ({address[0]}:{address[1]})")
        broadcast(f"\n[Servidor] {username} entrou no chat.\n", client_socket)
        client_socket.send(f"Bem-vindo ao chat, {username}! Digite 'exit' para sair.\n".encode('utf-8'))

        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8').strip()
                if not message:
                    break
                if message.lower() == 'exit':
                    break

                detected = detect_personal_data(message)
                
                if detected:
                    alert = f"\n[ALERTA GDPR] Mensagem bloqueada! Dados pessoais detetados: {', '.join(detected)}\n"
                    client_socket.send(alert.encode('utf-8'))
                    
                    save_personal_data(username, message, detected)
                    
                    print(f"[GDPR BLOCK] {username} tentou enviar dados sensíveis: {detected}")
                    print(f"   → Guardado em: {DATA_FILE}")
                    continue

                full_message = f"{username}: {message}"
                print(full_message)
                broadcast(full_message, client_socket)

            except:
                break

    except Exception as e:
        print(f"Erro com cliente {address}: {e}")
    finally:
        remove_client(client_socket)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(10)

print(f"Servidor GDPR Chat iniciado em {HOST}:{PORT}")
print(f"Dados pessoais serão guardados em: {DATA_FILE}")
print("Aguardando conexões... (Ctrl+C para parar)\n")

try:
    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.daemon = True
        thread.start()
except KeyboardInterrupt:
    print("\nServidor encerrado pelo utilizador.")
finally:
    server.close()