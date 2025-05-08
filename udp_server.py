import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 12345))
print("UDP Server is listening...")

data, addr = s.recvfrom(1024)
print("Received from", addr, ":", data.decode())

s.sendto(b"ACK", addr)
