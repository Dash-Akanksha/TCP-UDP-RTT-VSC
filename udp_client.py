import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Hello Server", ('localhost', 12345))

data, addr = s.recvfrom(1024)
print("Received from server:", data.decode())
