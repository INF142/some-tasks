from socket import socket, AF_INET, SOCK_DGRAM


sock = socket(AF_INET, SOCK_DGRAM)

server_address = ("localhost", 5555)
while (key_pressed:=input("> ")) in "wasd":
  sock.sendto(key_pressed.encode(), server_address)
  pos, _ = sock.recvfrom(2)
  print(f"x: {pos[0]}; y: {pos[1]}")

sock.sendto(b"c", server_address)
