from socket import socket, SOL_SOCKET, SO_REUSEADDR

sock = socket()
# Reuse an address
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("localhost", 5555))
sock.listen()
print('The server is ready to receive')
while True:
  conn, _ = sock.accept()
  sentence = conn.recv(1024).decode()
  new_sentence = sentence.upper()
  conn.send(new_sentence.encode())
  conn.close()
