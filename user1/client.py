import socket
from threading import Thread


def send_func():
    while True:
     message = input("Write message to server:")
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server_address = ('localhost', 12345)
     client_socket.connect(server_address)
     client_socket.send(message.encode('utf-8'))
     response = client_socket.recv(1024).decode('utf-8')
     print(f"Server: {response}")
     client_socket.close()

send_thread = Thread(target=send_func())
send_thread.start()