from socket import socket, AF_INET, SOCK_DGRAM


sock = socket(AF_INET, SOCK_DGRAM)

data = "nice!".encode()
for _ in range(5):
  size = sock.sendto(data, ("localhost", 5555))
  print(f"Sent {size} bytes")
