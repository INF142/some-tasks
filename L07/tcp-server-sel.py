from selectors import DefaultSelector, EVENT_READ
from socket import socket, SOL_SOCKET, SO_REUSEADDR


def accept(sock):
  conn, address = sock.accept()  # Should be ready
  print('accepted', conn, 'from', address)
  conn.setblocking(False)
  sel.register(conn, EVENT_READ)


def read(conn):
  data = conn.recv(1024)  # Should be ready
  if data:
    sentence = data.decode()
    new_sentence = sentence.upper()
    conn.send(new_sentence.encode())
  else:
    print('closing', conn)
    sel.unregister(conn)
    conn.close()


sel = DefaultSelector()
sock = socket()
# Reuse an address
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("localhost", 5555))
sock.listen()
sock.setblocking(False)
sel.register(sock, EVENT_READ, True)

while True:
  events = sel.select()
  for key, _ in events:
    if key.data:
      accept(key.fileobj)
    else:
      read(key.fileobj)
