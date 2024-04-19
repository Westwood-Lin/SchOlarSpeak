import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(1)
    print("Server started, waiting for connections...")
    global client_socket
    client_socket, addr = server.accept()
    print("Connected by", addr)

def send_message(msg):
    global client_socket
    message = msg.encode('utf-8')
    client_socket.sendall(message)
    print(f"Sent: {msg}")

def close_server():
    global client_socket
    client_socket.close()