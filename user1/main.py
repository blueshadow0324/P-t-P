import socket

while True:
 server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 server_socket.bind(('0.0.0.0', 49152))
 server_socket.listen(5)
 print("Server is listening...")
 client_socket, client_address = server_socket.accept()
 print(f"Connected to: {client_address}")
 message = client_socket.recv(1024).decode('utf-8')
 print(message)
 client_socket.send("Message received!".encode('utf-8'))

 client_socket.close()
 server_socket.close()