from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
from positioning import *


sock = socket(AF_INET, SOCK_DGRAM)
# Reuse an address
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("localhost", 5555))

x = 128
y = 128

while True:
  key_pressed, address = sock.recvfrom(1)
  if key_pressed == b"c":
    break
  x, y = positioning(key_pressed, x, y)
  sock.sendto(bytes((x, y)), address)
