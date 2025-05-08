import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))
s.listen(1)
print("Server is listening...")

conn, addr = s.accept()
print("Connection established with", addr)

data = conn.recv(1024)
print("Received:", data.decode())

conn.sendall(b"ACK")
conn.close()
