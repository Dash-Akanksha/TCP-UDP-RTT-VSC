import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_var = 12345
client_socket.connect(('localhost', new_var))

client_socket.send("Hello Server!".encode())
response = client_socket.recv(1024).decode()
print("Response from server:", response)

client_socket.close()
