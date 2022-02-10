from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR


sock = socket(AF_INET, SOCK_DGRAM)
# Reuse an address
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("localhost", 5555))

for size in range(1, 6):
  data, _ = sock.recvfrom(size)
  message = data.decode()
  print(f"Received message: {message}")
